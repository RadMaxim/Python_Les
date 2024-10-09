import cv2
import os

content = os.listdir("img")
for j,i in enumerate(content,0):
    # print(j,i)
    selected = int(input(f"Select any color img number {j+1}: 1 - COLOR_BGR2RGB, 2 -COLOR_BGR2HSV, 3 - COLOR_BGR2GRAY, 4- COLOR_BGR2HLS"))
    img1 = cv2.imread("img/" + str(i))
    img2 = cv2.imread("img/" + str(i))
    if selected == 1:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    elif selected == 2:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    elif selected == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    elif selected == 4:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HLS)
    else:
        print("Такого выбора нет")
    cv2.imshow("img_selected", img1)
    cv2.imshow("img1", img2)
    cv2.waitKey(0)
