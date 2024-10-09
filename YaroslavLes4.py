import cv2
img1 = cv2.imread("img/nick_memasik.png")
# select = int(input("Сделать выбор : 1 - bgr , 2 - hsv, 3 - gray:       "))
img6 = cv2.cvtColor(img1,cv2.COLOR_BGR2HLS)
img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
img3 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img4 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img5 = cv2.cvtColor(img1,cv2.COLOR_BGR2LAB)


cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("img3",img3)
cv2.imshow("img4",img4)
cv2.imshow("img5",img5)
cv2.imshow("img",img6)

cv2.waitKey(0)
