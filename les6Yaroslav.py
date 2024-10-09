# import cv2,os,numpy,datetime
# times_hour = datetime.datetime.now().hour
# times_min = datetime.datetime.now().minute
# times_sec = datetime.datetime.now().second
#
# print(times_hour,times_min,times_sec)
# imgs = os.listdir("img")
# img = cv2.imread(f"img/{imgs[0]}")
# # img_flip = cv2.flip(img,1)
# # angle = int(input("Введите колличество градусов"))
# # img_numpy = numpy.rot90(img,angle//90)
# # cv2.imshow("img",img)
# # cv2.imshow("numpy",img_numpy)
# # cv2.imshow("flip",img_flip)
# # cv2.waitKey(0)
# # times_hour_finish = datetime.datetime.now().hour
# # times_min_finish = datetime.datetime.now().minute
# # times_sec_finish = datetime.datetime.now().second
# # print(times_hour_finish,times_min_finish,times_sec_finish)
# # wholeTimeSecond_start = times_sec+times_min*60+times_hour*60*60
# # wholeTimeSecond_finish = times_sec_finish+times_min_finish*60+times_hour_finish*60*60
# # workTime = 0
# # if times_sec_finish - times_sec>0:
# #     workTime = times_sec_finish - times_sec
# #     print(workTime)
# # else:
# #     workTime = 60-times_sec+times_sec_finish
# #     print(workTime)
# # print(f"Программа отработала секунд: {wholeTimeSecond_finish-wholeTimeSecond_start}")
# # for elem in range(1000000):
# #     time_sec = datetime.datetime.now().second
# #     cv2.waitKey(1000)
# #     print(time_sec)
# x1, x2 , y1 , y2 = 0,img.shape[1],0,img.shape[0]
# for elem in  range(100000000):
#     if x1 > 16:
#         print("Увеличиваем картинку ")
#         x1 = x1 - 2
#         y1 = y1 - 2
#         x2 = x2 + 2
#         y2 = y2 + 2
#     else:
#
#         print("Уменьшаем картинку")
#         x1 = x1+2
#         y1 = y1+2
#         x2 = x2-2
#         y2 = y2-2
#     img1 = img[y1:y2, x1:x2]
#
#     cv2.imshow("img",img1)
#     cv2.waitKey(1000)
import cv2,os,datetime
img = os.listdir("img")
times_first = datetime.datetime.now().second
max_img = cv2.imread(f"img/{img[0]}")
big = 0
for index,elem in enumerate(img,0):
    capture = cv2.imread(f"img/{elem}")
    cv2.imshow("img",capture)
    if max_img.shape[0]*max_img.shape[1]<capture.shape[0]*capture.shape[1]:
        big = index
        max_img = cv2.imread(f"img/{img[big]}")
    cv2.waitKey(1000)
times_second = datetime.datetime.now().second
cv2.imshow("big",max_img)
cv2.waitKey(0)
print(f"Программа отработала: {times_first-times_second} секунд. Всего в папке лежит {len(img)} картинок, самая большая из них под {big} индексом")