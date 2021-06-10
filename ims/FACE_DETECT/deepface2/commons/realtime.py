import os
from tqdm import tqdm
import numpy as np
import pandas as pd
import cv2
import time
import re
import operator
import pickle
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from ims.FACE_DETECT.deepface2 import DeepFace
from ims.FACE_DETECT.deepface2.extendedmodels import Age
from ims.FACE_DETECT.deepface2.commons import functions, realtime, distance as dst

def represent(img_path, model_name = 'VGG-Face', model = None, enforce_detection = True, detector_backend = 'mtcnn'):

    """
    This function represents facial images as vectors.

    Parameters:
        img_path: exact image path, numpy array or based64 encoded images could be passed.

        model_name (string): VGG-Face, Facenet, OpenFace, DeepFace, DeepID, Dlib, ArcFace.

        model: Built deepface model. A face recognition model is built every call of verify function. You can pass pre-built face recognition model optionally if you will call verify function several times. Consider to pass model if you are going to call represent function in a for loop.

            model = DeepFace.build_model('VGG-Face')

        enforce_detection (boolean): If any face could not be detected in an image, then verify function will return exception. Set this to False not to have this exception. This might be convenient for low resolution images.

        detector_backend (string): set face detector backend as mtcnn, opencv, ssd or dlib

    Returns:
        Represent function returns a multidimensional vector. The number of dimensions is changing based on the reference model. E.g. FaceNet returns 128 dimensional vector; VGG-Face returns 2622 dimensional vector.
    """

    if model is None:
        model = DeepFace.build_model(model_name)

    #---------------------------------

    #decide input shape
    input_shape =  input_shape_x, input_shape_y= functions.find_input_shape(model)

    #detect and align
    img = functions.preprocess_face(img = img_path
        , target_size=(input_shape_y, input_shape_x)
        , enforce_detection = enforce_detection
        , detector_backend = detector_backend)

    #represent
    embedding = model.predict(img)[0].tolist()

    return embedding


def analysis(db_path, model_name, distance_metric, enable_face_analysis = True
                , source = 0, time_threshold = 5, frame_threshold = 5):

    input_shape = (150, 150); input_shape_x = input_shape[0]; input_shape_y = input_shape[1]
    text_color = (255,255,255)
    employees = []
    
    #check passed db folder exists
    if os.path.isdir(db_path) == True:
        
        file_name = "representations_%s.pkl" % (model_name)
        file_name = file_name.replace("-", "_").lower()
        tic = time.time()
        if os.path.exists(db_path+"/"+file_name):
            print("WARNING: Representations for images in ",db_path," folder were previously stored in ", file_name, ". If you added new instances after this file creation, then please delete this file and call find function again. It will create it again.")
            f = open(db_path+'/'+file_name, 'rb')
            representations = pickle.load(f)

            print("There are ", len(representations)," representations found in ",file_name)
        else:
            employees = []

            for r, d, f in os.walk(db_path):  # r=root, d=directories, f = files
                for file in f:
                    if ('.jpg' in file.lower()) or ('.png' in file.lower()):
                        exact_path = r + "/" + file
                        employees.append(exact_path)

            if len(employees) == 0:
                raise ValueError("There is no image in ", db_path,
                                 " folder! Validate .jpg or .png files exist in this path.")

            # ------------------------
            #if len>0:


            # ------------------------
            model = DeepFace.build_model(model_name)
            print(model_name, " is built")  # dlib modelimiz get ile alındı ve yüklendi.
            input_shape = functions.find_input_shape(model)
            input_shape_x = input_shape[0]
            input_shape_y = input_shape[1]

            # tuned thresholds for model and metric pair
            threshold = dst.findThreshold(model_name, distance_metric)

            # find representations for db images
            representations = []

            
            pbar = tqdm(range(0, len(employees)), desc='Finding representations')

            # for employee in employees:
            for index in pbar:
                employee = employees[index]
                instance = []
                instance.append(employee)
                representation = represent(img_path=employee
                                           , model_name="Dlib",
                                            enforce_detection=False, detector_backend="opencv")

                instance.append(representation)

                # -------------------------------

                representations.append(instance)

            f = open(db_path + '/' + file_name, "wb")
            pickle.dump(representations, f)
            f.close()

            print("Representations stored in ", db_path, "/", file_name,
                  " file. Please delete this file when you add new identities in your database.")

        # ----------------------------
        
        threshold = dst.findThreshold(model_name, distance_metric)
        df = pd.DataFrame(representations, columns = ['employee', 'embedding'])
        df['distance_metric'] = distance_metric

        toc = time.time()

        print("Embeddings found for given data set in ", toc-tic," seconds")

    #-----------------------

    pivot_img_size = 112 #face recognition result image

    #-----------------------

    opencv_path = functions.get_opencv_path()
    face_detector_path = opencv_path+"haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(face_detector_path)

    #-----------------------

    freeze = False
    face_detected = False
    face_included_frames = 0 #freeze screen if face detected sequantially 5 frames
    freezed_frame = 0
    tic = time.time()

    cap = cv2.VideoCapture(source) #webcam
    recognized = {}
    
    
    # function to return key for any value
    def get_key(val):
        for key, value in recognized.items():
            if val == value:
                return key
    
        return "key doesn't exist"

    while(True):
        ret, img = cap.read()

        if img is None:
            break

        #cv2.namedWindow('img', cv2.WINDOW_FREERATIO)
        #cv2.setWindowProperty('img', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        raw_img = img.copy()
        resolution = img.shape

        resolution_x = img.shape[1]; resolution_y = img.shape[0]

        if freeze == False:
            faces = face_cascade.detectMultiScale(img, 1.3, 5)

            if len(faces) == 0:
                face_included_frames = 0
        else:
            faces = []

        detected_faces = []
        face_index = 0
        for (x,y,w,h) in faces:
            if w > 130: #discard small detected faces

                face_detected = True
                if face_index == 0:
                    face_included_frames = face_included_frames + 1 #increase frame for a single face

                cv2.rectangle(img, (x,y), (x+w,y+h), (67,67,67), 1) #draw rectangle to main image

                cv2.putText(img, str(frame_threshold - face_included_frames), (int(x+w/4),int(y+h/1.5)), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2)

                detected_face = img[int(y):int(y+h), int(x):int(x+w)] #crop detected face

                #-------------------------------------

                detected_faces.append((x,y,w,h))
                face_index = face_index + 1

                #-------------------------------------

        if face_detected == True and face_included_frames == frame_threshold and freeze == False:
            freeze = True
            #base_img = img.copy()
            base_img = raw_img.copy()
            detected_faces_final = detected_faces.copy()
            tic = time.time()

        if freeze == True:

            toc = time.time()
            if (toc - tic) < time_threshold:

                if freezed_frame == 0:
                    freeze_img = base_img.copy()
                    #freeze_img = np.zeros(resolution, np.uint8) #here, np.uint8 handles showing white area issue

                    for detected_face in detected_faces_final:
                        x = detected_face[0]; y = detected_face[1]
                        w = detected_face[2]; h = detected_face[3]

                        cv2.rectangle(freeze_img, (x,y), (x+w,y+h), (67,67,67), 1) #draw rectangle to main image

                        #-------------------------------

                        #apply deep learning for custom_face

                        custom_face = base_img[y:y+h, x:x+w]

                        #-------------------------------
                        #facial attribute analysis

                        if enable_face_analysis == False:

                            gray_img = functions.preprocess_face(img = custom_face, target_size = (48, 48), grayscale = True, enforce_detection = False)
                            emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
                            emotion_predictions = emotion_model.predict(gray_img)[0,:]
                            sum_of_predictions = emotion_predictions.sum()

                            mood_items = []
                            for i in range(0, len(emotion_labels)):
                                mood_item = []
                                emotion_label = emotion_labels[i]
                                emotion_prediction = 100 * emotion_predictions[i] / sum_of_predictions
                                mood_item.append(emotion_label)
                                mood_item.append(emotion_prediction)
                                mood_items.append(mood_item)

                            emotion_df = pd.DataFrame(mood_items, columns = ["emotion", "score"])
                            emotion_df = emotion_df.sort_values(by = ["score"], ascending=False).reset_index(drop=True)

                            #background of mood box

                            #transparency
                            overlay = freeze_img.copy()
                            opacity = 0.4

                            if x+w+pivot_img_size < resolution_x:
                                #right
                                cv2.rectangle(freeze_img
                                    #, (x+w,y+20)
                                    , (x+w,y)
                                    , (x+w+pivot_img_size, y+h)
                                    , (64,64,64),cv2.FILLED)

                                cv2.addWeighted(overlay, opacity, freeze_img, 1 - opacity, 0, freeze_img)

                            elif x-pivot_img_size > 0:
                                #left
                                cv2.rectangle(freeze_img
                                    #, (x-pivot_img_size,y+20)
                                    , (x-pivot_img_size,y)
                                    , (x, y+h)
                                    , (64,64,64),cv2.FILLED)

                                cv2.addWeighted(overlay, opacity, freeze_img, 1 - opacity, 0, freeze_img)

                            for index, instance in emotion_df.iterrows():
                                emotion_label = "%s " % (instance['emotion'])
                                emotion_score = instance['score']/100

                                bar_x = 35 #this is the size if an emotion is 100%
                                bar_x = int(bar_x * emotion_score)

                                if x+w+pivot_img_size < resolution_x:

                                    text_location_y = y + 20 + (index+1) * 20
                                    text_location_x = x+w

                                    if text_location_y < y + h:
                                        cv2.putText(freeze_img, emotion_label, (text_location_x, text_location_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

                                        cv2.rectangle(freeze_img
                                            , (x+w+70, y + 13 + (index+1) * 20)
                                            , (x+w+70+bar_x, y + 13 + (index+1) * 20 + 5)
                                            , (255,255,255), cv2.FILLED)

                                elif x-pivot_img_size > 0:

                                    text_location_y = y + 20 + (index+1) * 20
                                    text_location_x = x-pivot_img_size

                                    if text_location_y <= y+h:
                                        cv2.putText(freeze_img, emotion_label, (text_location_x, text_location_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

                                        cv2.rectangle(freeze_img
                                            , (x-pivot_img_size+70, y + 13 + (index+1) * 20)
                                            , (x-pivot_img_size+70+bar_x, y + 13 + (index+1) * 20 + 5)
                                            , (255,255,255), cv2.FILLED)

                            #-------------------------------

                            face_224 = functions.preprocess_face(img = custom_face, target_size = (224, 224), grayscale = False, enforce_detection = False)

                            age_predictions = age_model.predict(face_224)[0,:]
                            apparent_age = Age.findApparentAge(age_predictions)

                            #-------------------------------

                            gender_prediction = gender_model.predict(face_224)[0,:]

                            if np.argmax(gender_prediction) == 0:
                                gender = "W"
                            elif np.argmax(gender_prediction) == 1:
                                gender = "M"

                            #print(str(int(apparent_age))," years old ", dominant_emotion, " ", gender)

                            analysis_report = str(int(apparent_age))+" "+gender

                            #-------------------------------

                            info_box_color = (46,200,255)

                            #top
                            if y - pivot_img_size + int(pivot_img_size/5) > 0:

                                triangle_coordinates = np.array( [
                                    (x+int(w/2), y)
                                    , (x+int(w/2)-int(w/10), y-int(pivot_img_size/3))
                                    , (x+int(w/2)+int(w/10), y-int(pivot_img_size/3))
                                ] )

                                cv2.drawContours(freeze_img, [triangle_coordinates], 0, info_box_color, -1)

                                cv2.rectangle(freeze_img, (x+int(w/5), y-pivot_img_size+int(pivot_img_size/5)), (x+w-int(w/5), y-int(pivot_img_size/3)), info_box_color, cv2.FILLED)

                                cv2.putText(freeze_img, analysis_report, (x+int(w/3.5), y - int(pivot_img_size/2.1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 111, 255), 2)

                            #bottom
                            elif y + h + pivot_img_size - int(pivot_img_size/5) < resolution_y:

                                triangle_coordinates = np.array( [
                                    (x+int(w/2), y+h)
                                    , (x+int(w/2)-int(w/10), y+h+int(pivot_img_size/3))
                                    , (x+int(w/2)+int(w/10), y+h+int(pivot_img_size/3))
                                ] )

                                cv2.drawContours(freeze_img, [triangle_coordinates], 0, info_box_color, -1)

                                cv2.rectangle(freeze_img, (x+int(w/5), y + h + int(pivot_img_size/3)), (x+w-int(w/5), y+h+pivot_img_size-int(pivot_img_size/5)), info_box_color, cv2.FILLED)

                                cv2.putText(freeze_img, analysis_report, (x+int(w/3.5), y + h + int(pivot_img_size/1.5)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 111, 255), 2)

                        #-------------------------------
                        #face recognition

                        custom_face = functions.preprocess_face(img = custom_face, target_size = (input_shape_y, input_shape_x), enforce_detection = False)
                        
                        #check preprocess_face function handled
                        if custom_face.shape[1:3] == input_shape:
                            if df.shape[0] > 0: #if there are images to verify, apply face recognition
                                img1_representation = model.predict(custom_face)[0,:]

                                #print(freezed_frame," - ",img1_representation[0:5])

                                def findDistance(row):
                                    distance_metric = row['distance_metric']
                                    img2_representation = row['embedding']

                                    distance = 1000 #initialize very large value
                                    if distance_metric == 'cosine':
                                        distance = dst.findCosineDistance(img1_representation, img2_representation)
                                    elif distance_metric == 'euclidean':
                                        distance = dst.findEuclideanDistance(img1_representation, img2_representation)
                                    elif distance_metric == 'euclidean_l2':
                                        distance = dst.findEuclideanDistance(dst.l2_normalize(img1_representation), dst.l2_normalize(img2_representation))

                                    return distance

                                df['distance'] = df.apply(findDistance, axis = 1)
                                df = df.sort_values(by = ["distance"])

                                candidate = df.iloc[0]
                                employee_name = candidate['employee']
                                best_distance = candidate['distance']

                                #print(candidate[['employee', 'distance']].values)
                                print("best_distance=",best_distance)
                                #if True:
                                if best_distance <= threshold:
                                    #print("best_distance=",best_distance)
                                    print("threshold=",threshold)
                                    #print(employee_name)
                                    display_img = cv2.imread(employee_name)

                                    display_img = cv2.resize(display_img, (pivot_img_size, pivot_img_size))

                                    label = employee_name.split("/")[-2].replace(".jpg", "")
                                    #label = re.sub('[0-9]', '', label)
                                    label = label.split("\\")[-1]
                                    
                                    #print(label)
                                    if label in recognized:
                                
                                        number = recognized[label]+1
                                        recognized[label]=number
                                        
        
                                    else:
                                        recognized[label] = 1
                                    
                                    print(recognized)
                                                            

                                    try:
                                        if y - pivot_img_size > 0 and x + w + pivot_img_size < resolution_x:
                                            #top right
                                            freeze_img[y - pivot_img_size:y, x+w:x+w+pivot_img_size] = display_img

                                            overlay = freeze_img.copy(); opacity = 0.4
                                            cv2.rectangle(freeze_img,(x+w,y),(x+w+pivot_img_size, y+20),(46,200,255),cv2.FILLED)
                                            cv2.addWeighted(overlay, opacity, freeze_img, 1 - opacity, 0, freeze_img)

                                            cv2.putText(freeze_img, label, (x+w, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)

                                            #connect face and text
                                            cv2.line(freeze_img,(x+int(w/2), y), (x+3*int(w/4), y-int(pivot_img_size/2)),(67,67,67),1)
                                            cv2.line(freeze_img, (x+3*int(w/4), y-int(pivot_img_size/2)), (x+w, y - int(pivot_img_size/2)), (67,67,67),1)

                                        elif y + h + pivot_img_size < resolution_y and x - pivot_img_size > 0:
                                            #bottom left
                                            freeze_img[y+h:y+h+pivot_img_size, x-pivot_img_size:x] = display_img

                                            overlay = freeze_img.copy(); opacity = 0.4
                                            cv2.rectangle(freeze_img,(x-pivot_img_size,y+h-20),(x, y+h),(46,200,255),cv2.FILLED)
                                            cv2.addWeighted(overlay, opacity, freeze_img, 1 - opacity, 0, freeze_img)

                                            cv2.putText(freeze_img, label, (x - pivot_img_size, y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)

                                            #connect face and text
                                            cv2.line(freeze_img,(x+int(w/2), y+h), (x+int(w/2)-int(w/4), y+h+int(pivot_img_size/2)),(67,67,67),1)
                                            cv2.line(freeze_img, (x+int(w/2)-int(w/4), y+h+int(pivot_img_size/2)), (x, y+h+int(pivot_img_size/2)), (67,67,67),1)

                                        elif y - pivot_img_size > 0 and x - pivot_img_size > 0:
                                            #top left
                                            freeze_img[y-pivot_img_size:y, x-pivot_img_size:x] = display_img

                                            overlay = freeze_img.copy(); opacity = 0.4
                                            cv2.rectangle(freeze_img,(x- pivot_img_size,y),(x, y+20),(46,200,255),cv2.FILLED)
                                            cv2.addWeighted(overlay, opacity, freeze_img, 1 - opacity, 0, freeze_img)

                                            cv2.putText(freeze_img, label, (x - pivot_img_size, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)

                                            #connect face and text
                                            cv2.line(freeze_img,(x+int(w/2), y), (x+int(w/2)-int(w/4), y-int(pivot_img_size/2)),(67,67,67),1)
                                            cv2.line(freeze_img, (x+int(w/2)-int(w/4), y-int(pivot_img_size/2)), (x, y - int(pivot_img_size/2)), (67,67,67),1)

                                        elif x+w+pivot_img_size < resolution_x and y + h + pivot_img_size < resolution_y:
                                            #bottom righ
                                            freeze_img[y+h:y+h+pivot_img_size, x+w:x+w+pivot_img_size] = display_img

                                            overlay = freeze_img.copy(); opacity = 0.4
                                            cv2.rectangle(freeze_img,(x+w,y+h-20),(x+w+pivot_img_size, y+h),(46,200,255),cv2.FILLED)
                                            cv2.addWeighted(overlay, opacity, freeze_img, 1 - opacity, 0, freeze_img)

                                            cv2.putText(freeze_img, label, (x+w, y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)

                                            #connect face and text
                                            cv2.line(freeze_img,(x+int(w/2), y+h), (x+int(w/2)+int(w/4), y+h+int(pivot_img_size/2)),(67,67,67),1)
                                            cv2.line(freeze_img, (x+int(w/2)+int(w/4), y+h+int(pivot_img_size/2)), (x+w, y+h+int(pivot_img_size/2)), (67,67,67),1)
                                    except Exception as err:
                                        print(str(err))

                        tic = time.time() #in this way, freezed image can show 5 seconds

                        #-------------------------------

                time_left = int(time_threshold - (toc - tic) + 1)

                cv2.rectangle(freeze_img, (10, 10), (90, 50), (67,67,67), -10)
                cv2.putText(freeze_img, str(time_left), (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

                cv2.imshow('img', freeze_img)

                freezed_frame = freezed_frame + 1
            else:
                face_detected = False
                face_included_frames = 0
                freeze = False
                freezed_frame = 0

        else:
            cv2.imshow('img',img)
            
        
        #print(recognized)
        
       # try:
       #    certain = recognized.keys()[recognized.values().index(10)]
            
       #except:
              #   pass
        
        #print(certain)
        
        if 5 in recognized.values():
            #certain = recognized.keys()[recognized.values()].index(10)
            #print(certain)
            #print(get_key(5))
            
            cap.release()
            cv2.destroyAllWindows()
            return get_key(5)
            break
        
            
        if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit
            break
        
    #print(max(recognized.items(), key=operator.itemgetter(1))[0])
    #kill open cv things
    cap.release()
    cv2.destroyAllWindows()
