import  cv2
cam = cv2.VideoCapture(0)
def nth(a):
    pass
cv2.namedWindow("frame")
cv2.createTrackbar("low","frame",0,150,nth)
cv2.createTrackbar("hight","frame",50,255,nth)
while True:


    frame= cam.read()[1]
    low = cv2.getTrackbarPos("low","frame")
    hight = cv2.getTrackbarPos("hight","frame")
    print(low,hight)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
    mask = cv2.inRange(gray,low,hight)
    itog = cv2.bitwise_and(frame,mask,mask=mask)
    cv2.imshow("mask",mask)
    cv2.imshow("kj",itog)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    cv2.imshow("hsv",hsv)
    cv2.waitKey(1)