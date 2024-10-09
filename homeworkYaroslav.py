import cv2
img = cv2.imread("img/img6.jpg")
if img.shape[0]<300:
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
elif 800>img.shape[0]>=300:
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
elif img.shape[0]>800:
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)

cv2.imshow("img",img)
cv2.waitKey(0)