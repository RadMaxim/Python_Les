import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("setting")
def f(p):
   pass
cv2.createTrackbar("bH","setting",1,255,f)
cv2.createTrackbar("bL","setting",1,255,f)
cv2.createTrackbar("rH","setting",1,255,f)
cv2.createTrackbar("rL","setting",1,255,f)
cv2.createTrackbar("gL","setting",1,255,f)
cv2.createTrackbar("gH","setting",1,255,f)
while True:
   bL = cv2.getTrackbarPos("bL","setting")
   bH = cv2.getTrackbarPos("bH", "setting")
   rH = cv2.getTrackbarPos("rH", "setting")
   rL = cv2.getTrackbarPos("rL", "setting")
   gL = cv2.getTrackbarPos("gL", "setting")
   gH = cv2.getTrackbarPos("gH", "setting")
   frame = cam.read()[1]
   hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   green_min=(bL, gL, rL)
   green_max=(bH, gH, rH)
   res=cv2.inRange(hsv, green_min, green_max)
   cv2.imshow("setting", res)
   cv2.waitKey(1)