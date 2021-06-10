from background_task import background

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

from ims.FACE_DETECT.deepface2 import DeepFace
from ims.FACE_DETECT.deepface2.extendedmodels import Age
from ims.FACE_DETECT.deepface2.commons import functions, realtime, distance

@background(schedule=5)
def create_pickle_file(db_path, model_name, distance_metric, enable_face_analysis = True, 
                        source = 0, time_threshold = 5, frame_threshold = 5):
    print("oluşturrr")
    file_name = "representations_%s.pkl" % (model_name)
    file_name = file_name.replace("-", "_").lower()
    tic = time.time()
    
    model = DeepFace.build_model(model_name)
    print(model_name, " is built")  # dlib modelimiz get ile alındı ve yüklendi.

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

    input_shape = functions.find_input_shape(model)
    input_shape_x = input_shape[0]
    input_shape_y = input_shape[1]

    # tuned thresholds for model and metric pair
    threshold = distance.findThreshold(model_name, distance_metric)

    # find representations for db images
    representations = []

    
    pbar = tqdm(range(0, len(employees)), desc='Finding representations')
    # for employee in employees:
    for index in pbar:
        employee = employees[index]
        instance = []
        instance.append(employee)
        representation = realtime.represent(img_path=employee
                                    , model_name=model_name, model="Dlib"
                                    , enforce_detection=False, detector_backend="mtcnn")

        instance.append(representation)

        # -------------------------------

        representations.append(instance)

    f = open(db_path + '/' + file_name, "wb")
    pickle.dump(representations, f)
    f.close()
    print("Representations stored in ", db_path, "/", file_name,
            " file. Please delete this file when you add new identities in your database.")