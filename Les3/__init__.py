# 1)
# import cv2
# import numpy
# cam = cv2.VideoCapture(0)
# def fun(p):
#     pass
# cv2.namedWindow("rotate90",cv2.WINDOW_NORMAL)
# cv2.createTrackbar("setting", "rotate90",1,4,fun)
# listColor = [0,cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HLS, cv2.COLOR_BGR2RGB,cv2.COLOR_BGR2HSV]
# textColor = ["origin","GRAY","HLS","RGB","HSV"]
# while True:
#     setting = cv2.getTrackbarPos("setting","rotate90")
#     frame = cam.read()[1]
#     if setting>0:
#         frame = cv2.cvtColor(frame, listColor[setting])
#     cv2.putText(frame,textColor[setting],(200,200),1,5,(255,255,255),4)
#     cv2.imshow('rotate90',frame)
#     cv2.waitKey(1)
# 2)
# import cv2
# cam = cv2.VideoCapture(0)
# cv2.namedWindow("rotate90")
# cv2.namedWindow("rotate180")
# cv2.namedWindow("rotate270")
# while True:
#     frame = cam.read()[1]
#     img = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
#     cv2.imshow('rotate90',img)
#     img = cv2.rotate(img,cv2.ROTATE_180)
#     cv2.imshow('rotate180', img)
#     img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
#     cv2.imshow('rotate270', img)
#     cv2.waitKey(1)
# 3)
# import cv2
# cam = cv2.VideoCapture(0)
# cv2.namedWindow("fliph",cv2.WINDOW_NORMAL)
# cv2.namedWindow("flipv",cv2.WINDOW_NORMAL)
# cv2.namedWindow("fliphv",cv2.WINDOW_NORMAL)
# while True:
#     frame = cam.read()[1]
#     img = cv2.flip(frame,1)
#     cv2.imshow('fliph',img)
#     img = cv2.flip(frame,0)
#     cv2.imshow('flipv', img)
#     img = cv2.flip(frame,-1)
#     cv2.imshow('fliphv', img)
#     cv2.waitKey(1)
# 4)
# import cv2
# cam = cv2.VideoCapture(0)
# cv2.namedWindow("fliph",cv2.WINDOW_NORMAL)
# count = -1
# listColor = [cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HLS, cv2.COLOR_BGR2RGB]
# while True:
#
#     frame = cam.read()[1]
#     img = cv2.flip(frame,count)
#     img = cv2.cvtColor(img,listColor[count+1])
#     cv2.imshow('fliph',img)
#     count+=1
#     if count==2:
#         count=-1
#     cv2.waitKey(200)
# 5)
# import cv2
# cam = cv2.VideoCapture(0)
# def fun(p):
#     pass
# cv2.namedWindow("rotate90",cv2.WINDOW_NORMAL)
# cv2.createTrackbar("settingX0", "rotate90",1,400,fun)
# cv2.createTrackbar("settingY0", "rotate90",1,400,fun)
# cv2.createTrackbar("settingX1", "rotate90",3,400,fun)
# cv2.createTrackbar("settingY1", "rotate90",3,400,fun)
#
# while True:
#     settingX0 = cv2.getTrackbarPos("settingX0","rotate90")
#     settingX1 = cv2.getTrackbarPos("settingX1","rotate90")
#     settingY0 = cv2.getTrackbarPos("settingY0","rotate90")
#     settingY1 = cv2.getTrackbarPos("settingY1","rotate90")
#     frame = cam.read()[1]
#     setting = frame[settingX0:settingX1,settingY0:settingY1]
#     cv2.imshow('rotate90',frame)
#     cv2.imshow('setting',setting)
#     cv2.waitKey(1)