import cv2
# img = cv2.imread("./img/img4.jpg")
# (h,w,d) = img.shape
# print(h,w,d)
# bool = True
# for i in range(0,w,100):
#     for j in range(0,h,100):
#         cv2.rectangle(img,(i,j),(i+100,j+100),(150,0,10),1)
# cv2.imshow("img",img)
# cv2.waitKey(0)
import cv2
cv2.namedWindow("filter")
cam = cv2.VideoCapture(0)
def noth(n):
    pass
cv2.createTrackbar("hl","filter",0,255,noth)
cv2.createTrackbar("sl","filter",0,255,noth)
cv2.createTrackbar("vl","filter",0,255,noth)
cv2.createTrackbar("hh","filter",0,255,noth)
cv2.createTrackbar("sh","filter",0,255,noth)
cv2.createTrackbar("vh","filter",0,255,noth)
cv2.createTrackbar("seach","filter",0,10000,noth)

while True:
   img = cam.read()[1]
   hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   hl = cv2.getTrackbarPos("hl","filter")
   sl = cv2.getTrackbarPos("sl","filter")
   vl = cv2.getTrackbarPos("vl","filter")
   hh = cv2.getTrackbarPos("hh","filter")
   sh = cv2.getTrackbarPos("sh","filter")
   vh = cv2.getTrackbarPos("vh","filter")
   seach = cv2.getTrackbarPos("seach","filter")
   mint_low = (110, 65, 66)
   mint_high = (127, 138, 169)
   mask = cv2.inRange(hsv, mint_low, mint_high)
   res = cv2.bitwise_and(img, img, mask=mask)
   contours,hierarchy = cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
   for contour in contours:
       area = cv2.contourArea(contour)
       print(contour)
       print(area)
       if area>seach:
           x,y,w,h=cv2.boundingRect(contour)
           frame=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   cv2.imshow("img",img)
   cv2.imshow("filter2",res)
   cv2.imshow("mask", mask)
   cv2.waitKey(1)
