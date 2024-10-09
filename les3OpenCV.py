import cv2
img = cv2.imread("img/img1.jpg")
color = cv2.COLOR_BGR2HLS
selected = int(input("1-BGR2HSV, 2-BGR2GRAY, 3-BGR2HLS"))
if selected==1:
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
elif selected==2:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
elif selected==3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
else:
    print("Нет такого варианта")
cv2.imshow("result",img)
cv2.waitKey(0)

