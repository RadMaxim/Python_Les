import cv2
img1= cv2.imread("img/img6.jpg")
print(len(img1))
print(img1.shape)
cv2.imshow("window",img1)
cv2.waitKey(0)
