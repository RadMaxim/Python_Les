import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outputnew.avi',fourcc, 30.0, (640,480))

while True:
   ret, frame = cap.read()
   out.write(frame)
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) == ord('q'):
       break
cap.release()#выход из видеопотока
out.release()#выход из метода записи
cv2.destroyAllWindows()#закрываем все окна

