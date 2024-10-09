import cv2, numpy, os
imgs = os.listdir("img")
for elem in imgs:
    img = cv2.imread(f"img/{elem}")
    cv2.imshow(f"{elem}",img)
    cv2.waitKey(1)