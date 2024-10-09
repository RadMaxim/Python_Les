import cv2, datetime, numpy
cam = cv2.VideoCapture(0)
count_frame = 0
times_past = 0
count_keydown = 0
while True:
    times = datetime.datetime.now().second
    if times-times_past>=1:
        times_past = times
        speed = count_frame
        print(speed)
        count_frame=0
    count_frame+=1
    frame = cam.read()[1]
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.putText(gray,str(count_keydown),(50,50),1,1.5,(0,0,0),1)
    cv2.imshow("gray",gray)
    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)
    print(key)
    if key == 113:
        print("Вы нажали клавишу 113")
        break
    cv2.waitKey(1)
