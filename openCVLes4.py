import cv2,os
import mipe
imgs = os.listdir("img")
state = True
img = cv2.imread(f"img/{imgs[1]}")
img1 = cv2.flip(img,90)
x0 = 0
y0 = 0
x1 = img.shape[1]
y1 = img.shape[0]
for i in range(100):
    x0+=1
    y0+=1
    x1-=1
    y1-=1
    img = img[y0:y1, x0:x1]
    cv2.imshow("img",img)
    cv2.waitKey(100)




