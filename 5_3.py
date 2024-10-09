import cv2, datetime
cam = cv2.VideoCapture(0)
count = 0
def times():
    return (datetime.datetime.now().second,datetime.datetime.now().minute,datetime.datetime.now().hour)
red = (0,0,255)
blue = (255,0,0)
while True:
    t1 = datetime.datetime.now().second
    frame = cam.read()[1]
    cv2.putText(
        img=frame,
        text=f"{times()[2]}:{times()[1]}:{times()[0]}",
        org=(50,50),
        fontFace=1,
        fontScale=2,
        color=red,
        thickness=2)
    cv2.rectangle(img=frame,pt1=(20,20), pt2=(200,200),color=blue,thickness=2)
    cv2.imshow("frame",frame)

    cv2.waitKey(1)


