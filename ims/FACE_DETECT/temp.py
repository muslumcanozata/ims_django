# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from deepface2 import DeepFace
result = DeepFace.stream("FaceImages",model_name ='Dlib',time_threshold = 1, frame_threshold = 5)
print(result,"Kisisi tespit edildi")