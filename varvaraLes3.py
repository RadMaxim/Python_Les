import cv2 #подключение библиотеки для работы с изображениями
cam = cv2.VideoCapture(0)#подключение видеокамеры по адресу 0
size = 0
while True: #цикл, который постоянно работает
    size+=0.02
    frame = cam.read()[1]#запись каждого кадра в переменную frame
    cv2.waitKey(1)#задержка между перезапесью
    cv2.putText(frame,"text",(50,50),fontScale=size,color=(100,100,100),thickness=1)
    cv2.imshow("frame",frame)
    print(frame)
