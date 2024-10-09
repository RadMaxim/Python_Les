import cv2,datetime,os
cam = cv2.VideoCapture(0)
count = 0
frame1 = cam.read()[1]
while True:
    dateT = datetime.datetime.now()
    frame = cam.read()[1]
    cv2.putText(frame, str(dateT),(10,50), cv2.FONT_HERSHEY_SIMPLEX,1.2, (255,0, 0),3)
    code_key = cv2.waitKey(1)
    if code_key == 119:
        count += 1
    if count == 1:
        frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif count == 0:
        frame1 = frame
    elif count == 2:
        frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    elif count == 3:
        frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    elif count == 4:
        count = 0
    cv2.imshow("frame", frame1)
    if code_key==101:
        cv2.imwrite(f"photo_frame/photo_frame_{dateT.minute}_{dateT.second}.png",frame1)
    cv2.waitKey(1)
    if code_key == 113:
        print("программа завершила свою работу, вы нажали на r")
        break
imgs = os.listdir("photo_frame")
print(imgs)