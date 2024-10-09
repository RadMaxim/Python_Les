import os, cv2, numpy
array_img = os.listdir("./img")
print(array_img)
size = 50
for elem in array_img:
    img = cv2.imread(f"img/{elem}")
    print(img.shape)
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = numpy.rot90(gray,1)
    y = img.shape[0]//2
    x = img.shape[1]//2
    cv2.rectangle(img,(x-size,y-size),(x+size,y+size),thickness=2,color=(0,0,0))
    cv2.putText(img,"hello",(x,y),1,2.5,(0,0,255),2)
    print(x,y)
    cv2.imshow("img",img)
    cv2.imshow("gray",gray)
    cv2.waitKey(1000)
    size+=10
