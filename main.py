import cv2
cam = cv2.VideoCapture(0)
while True:
    frame = cam.read()[1]
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("frame",gray)
    cv2.imshow("frame1",hsv)
    cv2.waitKey(1)