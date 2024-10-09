# 2 часть уркоа - https://drive.google.com/drive/u/1/folders/14ATyc5zWKTY6kVTSrZQgw4Phf5wKKCMc
# Создание дата сета, модели, для нахождения лица вашего
#opencv-contrib-puthon
#opencv-python
#image
#Python 3.10
#Одной версии должны быть.
# модель универсальная, может несколько лиц сразу распознавать и читать

import cv2
import numpy as np
from PIL import Image
import os

path = 'img'

recognizer = cv2.face.LBPHFaceRecognizer()

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

def getImagesAndLabels(path):

   imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
   faceSamples=[]
   ids = []

   for imagePath in imagePaths:

       PIL_img = Image.open(imagePath).convert('L') # преобразование в серые цвета
       img_numpy = np.array(PIL_img,'uint8')

       id = int(os.path.split(imagePath)[-1].split(".")[1])
       faces = detector.detectMultiScale(img_numpy)

       for (x,y,w,h) in faces:
           faceSamples.append(img_numpy[y:y+h,x:x+w])
           ids.append(id)

   return faceSamples,ids

print ("Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
recognizer.write('./model/trainer.yml')
print("{0} faces trained. Exiting Program".format(len(np.unique(ids))))
