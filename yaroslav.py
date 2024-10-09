import cv2
cascad_face = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")#подключили каскад Хаара для обнаружения лиц
cam = cv2.VideoCapture(0)#подключаем видеокамеру
while True: # для постоянной работы программы
    frame = cam.read()[1]# записываем кадр с вебкамеры
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)# преобразовали в серый цвет изображение
    faces = cascad_face.detectMultiScale(gray,1.3,5)# находим лица (координаты с высотой и шириной)
    if len(faces)==1:
        print("на камере 1 лицо")
    elif len(faces)==2:
        print("на камере 2 лица")
    for (x,y,w,h) in faces: # перебираем с помощью цикла все лица на вебке
        print(f"x: {x}, y: {y}, w: {w}, h: {h}")
        cv2.rectangle(frame,(x,y),(x+30,y+30),(0,0,0),2)# отрисовываем прямоугольник вокруг лица
        cv2.putText(frame,(f"x: {x}, y: {y}"),(x,y),1,1.2,(150,150,150),1)
    cv2.imshow("frame",frame)# показываем окно
    cv2.waitKey(1)

