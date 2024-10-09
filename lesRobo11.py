import cv2
image_file = "img/text.png"
cv2.namedWindow("window")
def noth(n):
    pass
cv2.createTrackbar("min","window",0,255,noth)
cv2.createTrackbar("max","window",0,255,noth)
while True:
    img = cv2.imread(image_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    minV = cv2.getTrackbarPos("min","window")
    maxV = cv2.getTrackbarPos("max","window")
    print(minV,maxV)
    ret, thresh = cv2.threshold(gray, minV, maxV, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
       (x, y, w, h) = cv2.boundingRect(contour)
       cv2.rectangle(img, (x, y), (x + w, y + h), (70, 0, 0), 1)
    cv2.imshow("res",thresh)
    cv2.imshow("Output", img)
    cv2.waitKey(1)
