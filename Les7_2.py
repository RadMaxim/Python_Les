import cv2
cap=cv2.VideoCapture(0)

def nothing(self):
   pass
cv2.namedWindow("filter")
cv2.createTrackbar("Hue","filter",0,255,nothing)
cv2.createTrackbar("Saturation","filter",0,255,nothing)
cv2.createTrackbar("Value","filter",0,255,nothing)
cv2.createTrackbar("HueH","filter",0,255,nothing)
cv2.createTrackbar("SaturationH","filter",0,255,nothing)
cv2.createTrackbar("ValueH","filter",0,255,nothing)
while True:
   ret,frame=cap.read()
   hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   h_l=cv2.getTrackbarPos("Hue","filter")
   s_l=cv2.getTrackbarPos("Saturation","filter")
   v_l=cv2.getTrackbarPos("Value","filter")
   h_h = cv2.getTrackbarPos("HueH", "filter")
   s_h = cv2.getTrackbarPos("SaturationH", "filter")
   v_h = cv2.getTrackbarPos("ValueH", "filter")
   lower=(h_l,s_l,v_l)
   higher=(h_h,s_h,v_h)
   result_data = f"h_h:{h_h}, s_h:{s_h}, v_h:{v_h}, h_l: {h_l}, s_l:{s_l}, v_l:{v_l}"
   cv2.putText(frame, result_data, (50,50), 1, 1, (255,255, 255), 1)
   cv2.imshow("filter", frame)
   cv2.waitKey(1)