import cv2

cap = cv2.VideoCapture(0)

count = 0
while True:

   ret, frame = cap.read()
   cv2.putText(frame, f"number photo {count}",(100,100), 1, 1, (255,255,255),1)
   cv2.imshow('frame',frame)
   cv2.waitKey(1)
   if cv2.waitKey(1) == ord('q'):
      count += 1
      cv2.imwrite(f'imgsFrame/frame_{count}.png',frame)

