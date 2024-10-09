import cv2
cascad_faces =  cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
video = cv2.VideoCapture("./video/faces.mp4")
while True:
    _,frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faces = cascad_faces.detectMultiScale(gray,scaleFactor=3,minSize=(5,5))
    for face in faces:
        (x,y,w,h) = face
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,0),2)
    print(faces)
    cv2.imshow("frame",frame)
    # cv2.imshow("rgb", rjb)
    cv2.waitKey(1)