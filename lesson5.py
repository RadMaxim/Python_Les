import cv2, os
img_list = os.listdir("img")
img = cv2.imread(f"img/{img_list[0]}")
print(img.shape)
y1 = int(input("y1 : "))
y2 = int(input("y2 : "))
while y1>y2:
    print("Не верный промежуток по высоте, введите заново")
    y1 = int(input("y1 : "))
    y2 = int(input("y2 : "))
x1 = int(input("x1 : "))
x2 = int(input("x2 : "))
count = 0
while x1>x2:
    count+=1
    if count>2:
        print("Хватит дурачиться")
    else:
        print("Не верный промежуток по ширине, введите заново")
    x1 = int(input("x1 : "))
    x2 = int(input("x2 : "))

img_cut = img[y1:y2,x1:x2]
cv2.imshow("img",img)
cv2.imshow("img_cut",img_cut)
cv2.waitKey(0)


