import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outOrigin = cv2.VideoWriter('outputOrigin.avi',fourcc, 30.0, (640,480))
outGray = cv2.VideoWriter('outputGray.avi',fourcc, 30.0, (640,480))
outHSV = cv2.VideoWriter('outputHSV.avi',fourcc, 30.0, (640,480))
outHLS = cv2.VideoWriter('outputHLS.avi',fourcc, 30.0, (640,480))

while True:
   ret, frame = cap.read()
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
   hls = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)
   outOrigin.write(frame)
   outHLS.write(hls)
   outGray.write(gray)
   outHSV.write(hsv)
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) == ord('q'):
       break
cap.release()#выход из видеопотока
outOrigin.release()#выход из метода записи
outGray.release()#выход из метода записи
outHSV.release()#выход из метода записи
outHLS.release()
cv2.destroyAllWindows()#закрываем все окна