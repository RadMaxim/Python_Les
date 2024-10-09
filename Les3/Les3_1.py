import cv2
cam = cv2.VideoCapture(0)
times = 0
while True:
    times+=1
    frame = cam.read()[1]
    if times==1:
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if times==2:
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)
        times=0
    cv2.imshow("fr",frame)
    cv2.waitKey(1000)
