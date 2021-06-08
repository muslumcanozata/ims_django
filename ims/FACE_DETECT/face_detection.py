import cv2
import os


face_cascade=cv2.CascadeClassifier("ims/FACE_DETECT/frontalface.xml")
path = 'ims/FACE_DETECT/FaceImages'


def create_folder(user):
    try:
        if not os.path.exists(path + '/' + user):
            os.makedirs(path + '/' + user)
            return True
        else:
            print("User already exist")
            return False
    except OSError:
        print('Error: Creating directory of data')
        
        
def save_image(path, img, i):
    s = "{0}face.jpg"
    s1 = path + '/' + s.format(i)
    cv2.imwrite(s1,img)
    

def get_face_images(username):
    cap = cv2.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)
    count = 0
    
    while True:
        _,img = cap.read()
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)
        
        for (x,y,w,h) in faces:
            
             if h>int(img.shape[0])/2 :
                print(img.shape)
                print("face detecting")
                cv2.putText(img,"Bekleyiniz..",(30,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(124,252,0),3)
                detected_face = img[y-20:y+h+20, x-20:x+w+20]
                try:
                    resized = cv2.resize(detected_face, (400,400), interpolation = cv2.INTER_AREA)
                except Exception as e:
                    print(str(e))
                    
                save_image((path + '/' + username), resized, count)
                count += 1  
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
             else:
                cv2.putText(img,"Kameraya Yaklasiniz!",(30,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),3)
    
        cv2.imshow('img',img)
        
        if count == 5:
            break
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    return True
    
    
def face_detect(username):
    result = create_folder(username)

    if(result == True):
        return get_face_images(username)


    
