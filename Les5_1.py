import cv2, datetime
cam = cv2.VideoCapture(0)
count = 0
t1 = datetime.datetime.now().second

while True:
    print(count)
    frame = cam.read()[1]
    cv2.imshow("frame",frame)
    count+=1
    cv2.waitKey(1)
    if count==100:
        break
t2 =int(datetime.datetime.now().second)
print(f"while: {(t2-t1)}")
count = 0
for i in range(100):
    print(count)
    frame = cam.read()[1]
    cv2.imshow("frame", frame)
    count += 1
    cv2.waitKey(1)
t3 = int(datetime.datetime.now().second)
print(f"for: {(t3-t2)}")