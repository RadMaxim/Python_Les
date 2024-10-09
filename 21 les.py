# 1 часть уркоа - https://drive.google.com/drive/u/1/folders/14ATyc5zWKTY6kVTSrZQgw4Phf5wKKCMc

import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
cap = cv2.VideoCapture(0)


while True:
   ret, img = cap.read()
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   faces = face_cascade.detectMultiScale(gray, 1.3, 1)

   for (x, y, w, h) in faces:
       cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)


       roi_gray = gray[y:y + h, x:x + w]




   cv2.imshow('img', img)
   cv2.waitKey(1)




