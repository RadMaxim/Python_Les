import cv2

face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier("haarcascade_eye.xml")
smile = cv2.CascadeClassifier("haarcascade_smile.xml")
img=cv2.imread("img/img4.jpg")
# cv2.imshow("full",img)
a = {1,2,3,4,5}
b = {3,4,5,6,7}
cam = cv2.VideoCapture(0)
print(a|b)
print(a&b)
print(dict(zip(a,b)))

# print(faces)
# print(eyes)
count = 0
while True:

    frame = cam.read()[1]
    faces = face.detectMultiScale(frame, 1.1, 1)
    eyes = eye.detectMultiScale(frame, 1.1, 1)
    smiles = smile.detectMultiScale(frame, 1.1, 5)
    for item1,item2 in zip(faces,eyes):
        frame=cv2.rectangle(frame,(item1[0],item1[1]),(item1[0]+item1[2],item1[1]+item1[3]),(255,0,0),1)
        frame=cv2.rectangle(frame,(item2[0],item2[1]),(item2[0]+item2[2],item2[1]+item2[3]),(255,0,0),1)

        # roi=frame[item1[1]:item1[1]+item1[3],item1[0]:item1[0]+item1[2]]
        # cv2.imshow("roi"+str(count),roi)
        # count+=1
    for x,y,w,h in smiles:
        frame = cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),1)

    cv2.imshow("face",frame)
    cv2.waitKey(0)
