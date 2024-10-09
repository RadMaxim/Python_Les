import cv2

img1 = cv2.imread("img/nick_memasik.png")
shape1 = img1.shape
print(shape1)
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)
cv2.imshow("img",img1)
cv2.imshow("gray",gray)
print(f"Первый элемент кортежа: {shape1[0]}")
if shape1[0] < 400 and shape1[1] < 400:
    print("Картинка маленького размера")
elif 400 <= shape1[0] < 800 and 400 <= shape1[1] <= 800:
    print("Средняя картинка")
else:
    print("Картинка большого размера")
