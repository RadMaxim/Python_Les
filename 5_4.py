import cv2, datetime
cam = cv2.VideoCapture(0)
count = 0
def times():
    return (datetime.datetime.now().second,datetime.datetime.now().minute,datetime.datetime.now().hour)
red = (0,0,255)
blue = (255,0,0)
shape = cam.read()[1].shape
x = 0
y=20
def rects(frame, shape):
    global blue
    for i in range(0,shape[1],100):
        cv2.rectangle(frame,pt1=(i,y),pt2=(i+100,y+100),color=blue,thickness=1)
        for j in range(0, shape[0], 100):
            cv2.rectangle(frame, pt1=(i, j), pt2=(i + 100, j + 100), color=blue, thickness=1)
while True:

    t1 = datetime.datetime.now().second
    frame = cam.read()[1]
    rects(frame, shape)
    cv2.rectangle(img=frame,pt1=(20,20), pt2=(200,200),color=blue,thickness=2)
    cv2.imshow("frame",frame)

    cv2.waitKey(1)


