import cv2
cap=cv2.VideoCapture(0)
RED = ((0,139,144),(11,255,226))
YELLOW = ((15,139,144),(34,255,226))
def nothing(self):
   pass
cv2.namedWindow("filter")
cv2.createTrackbar("Hue","filter",0,255,nothing)
cv2.createTrackbar("Saturation","filter",0,255,nothing)
cv2.createTrackbar("Value","filter",0,255,nothing)
cv2.createTrackbar("HueH","filter",0,255,nothing)
cv2.createTrackbar("SaturationH","filter",0,255,nothing)
cv2.createTrackbar("ValueH","filter",0,255,nothing)
(h1,w1, d) = cap.read()[1].shape
while True:
   ret,frame=cap.read()
   hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   mask_forRed = cv2.inRange(hsv, RED[0], RED[1])
   mask_forYellow = cv2.inRange(hsv, YELLOW[0], YELLOW[1])
   contours, hierarchy = cv2.findContours(mask_forRed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
   contours1, hierarchy1 = cv2.findContours(mask_forYellow, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
   for contour in contours:
      area = cv2.contourArea(contour)
      if area > 800:
         x, y, w, h = cv2.boundingRect(contour)
         frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
         position = ""
         cv2.putText(frame, "RED",(50,50),1,2,(0,0,255),2)
         if x>w1//2:
             position = "right"
         else:
             position = "left"
         cv2.putText(frame, f"position: {position}", (w1//2, h1//2),1, 3 , (255,0,0))


   cv2.imshow("filter",frame)
   cv2.waitKey(1)