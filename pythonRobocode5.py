import cv2, datetime,os
# img = os.listdir("img")
# times = datetime.datetime.now()
#
# print(f"Программа запустилась в {times.hour} часов, {times.minute} минут, {times.second} секунд")
# img = cv2.imread(f"img/{img[0]}")
# cv2.imshow("img",img)
# cv2.waitKey(0)
# times1 = datetime.datetime.now()
# print(f"Программа прекратила свою работу в {times1.hour} часов, {times1.minute} минут, {times1.second} секунд")
# print(f"Время работы программы {times1.hour-times.hour} часов, {times1.minute -times.minute } минут, {times1.second - times.second } секунд")
# times = datetime.datetime.now()
# for t in range(0,200,1):
#     times = datetime.datetime.now()
#     print(f"{times.hour} часов, {times.minute} минут, {times.second} секунд")
#     cv2.waitKey(1000)
cam = cv2.VideoCapture(0)
selected = 0
while True:
    frame = cam.read()[1]
    times1 = datetime.datetime.now().second
    if times1%10==0:
        print("Сделайте выбор цветовой палитры 1 - hsv, 2 - gray, 3 - natural")
        selected = int(input())
    if selected == 1:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif selected == 2:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    elif selected == 3:
        frame = frame
    cv2.imshow("frame",frame)
    cv2.waitKey(1)