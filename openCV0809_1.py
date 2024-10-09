import cv2

cv2.namedWindow("frame")


def noth(var):
    pass
cv2.createTrackbar("track_Low","frame",0,255,noth)
cv2.createTrackbar("track1_Low","frame",0,255,noth)
cv2.createTrackbar("track2_Low","frame",0,255,noth)
cv2.createTrackbar("track_Hight","frame",0,255,noth)
cv2.createTrackbar("track1_Hight","frame",0,255,noth)
cv2.createTrackbar("track2_Hight","frame",0,255,noth)
print("dfv")
while True:
    img = cv2.imread("img/img5.jpg")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l1 = cv2.getTrackbarPos("track_Low","frame")
    l2 = cv2.getTrackbarPos("track1_Low","frame")
    l3 = cv2.getTrackbarPos("track2_Low","frame")
    h1 = cv2.getTrackbarPos("track_Hight","frame")
    h2 = cv2.getTrackbarPos("track1_Hight","frame")
    h3 = cv2.getTrackbarPos("track2_Hight","frame")
    print(l1,l2,l3,h1,h2,h3)
    mask = cv2.inRange(hsv, (l1, l2, l3),
    (h1, h2, h3))

    green_color=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("rubick", mask)
    cv2.imshow("res", green_color)

    cv2.waitKey(1)