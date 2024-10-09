import cv2,numpy
# cam = cv2.VideoCapture(0)
# img = cv2.imread("img8/images.png")
img1 = cv2.imread("img8/png-transparent-arrow-computer-icons-black-and-white-arrows-angle-rectangle-triangle-thumbnail.png")
img = numpy.rot90(img1,1)
print(img.shape)
print(img1.shape)
res = cv2.bitwise_and(img,img1)
res1 = cv2.bitwise_or(img,img1)
res2 = cv2.bitwise_xor(img,img1)
final = cv2.vconcat([res,res1,res2])
final1 = cv2.hconcat([res,res1,res2])

cv2.imshow("res2", res2)
cv2.imshow("res1", res1)
cv2.imshow("res", res)
cv2.imshow("final",final)
cv2.imshow("final1",final1)
cv2.waitKey(0)
# while True:
#     frame = cam.read()[1]
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     hsl = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)


    # cv2.imshow("frame",frame)
    # cv2.imshow("gray",gray)
    # cv2.imshow("hsv",hsv)
    # cv2.imshow("hsl",hsl)


    # cv2.waitKey(10)
    # frame1 = cam.read()[1]

