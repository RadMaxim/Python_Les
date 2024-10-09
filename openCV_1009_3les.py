import os
import cv2



# Вывести оценки и имена с помощью цикла for 1 tesk
# any_array_marks = [5,7,10,7,8,9,6,9]
# for number,mark in enumerate(any_array_marks,1):
#     print(number,mark)
# any_array_names = ["Maxim","Petya","Oleg","Vlad","Dasha","Dima","Vika","Natasha"]
# for number,names in enumerate(any_array_names,1):
#     print(number,names)
# Делаем помощника для преподавателя 2 task
# for marks,names in zip(enumerate(any_array_marks,1), enumerate(any_array_names,1)):
#     print(marks,names)
#     print(f"У {marks[0]} ученика, которого зовут - {names[1]} в журнале стоит отметка - {marks[1]}")
#     if marks[1]<=4:
#         print("Ему нужно выучить материал")
#     elif 4<marks[1]<=7:
#         print("Он знает материал, но нужно его немного подучить")
#     elif 7<marks[1]<=10:
#         print("Он хорошо знает материал")
#     else:
#         print("Такой отметки в системе оценивания не существует, проверте журнал")
#Совместить два массива в один и сформировать словарь 3 task
# all_array = dict(zip(any_array_names,any_array_marks))
# print(all_array)
#Посчитать колличество каждой из оценок 4 task
# all_array = dict(zip(any_array_names,any_array_marks))
# obj = {}
# for item in all_array.items():
#     if item[1] in obj:
#         obj[item[1]]+=1
#     else:
#         obj[item[1]]=1
# print(obj)

# all_img = os.listdir("img")
# for i in all_img:
#
#     img1 = cv2.imread(f"img/{i}")
#     print(f"Размер текущей картинки: {img1.shape}")
#     y1 = int(input("Введите сколько нужно обрезать по вертикали 1"))
#     y2 = int(input("Введите сколько нужно обрезать по вертикали 2"))
#     x1 = int(input("Введите сколько нужно обрезать по горизонтали 1"))
#     x2 = int(input("Введите сколько нужно обрезать по горизонтали 2"))
#     img2 = img1[y1:y2,x1:x2]
#     cv2.imshow("result",img2)
#     cv2.imshow("img",img1)
#     cv2.waitKey(0)
# print(all_img)

# print(img1.shape)
# img2 = img1[::-1]
# img3 = img1[100:438,200:600] #первая отрезок обрезает по вертикали,
#
# cv2.imshow("img2",img1)
# cv2.imshow("img3",img3)


import cv2

img1= cv2.imread("img/img6.jpg")
print("Первая картинка")
cv2.imshow("window",img1)
cv2.waitKey(0)
if len(img1)>1000:
    print("Большая картинка")
else:
    print("Маленькая картинка")
img2= cv2.imread("img/img3.jpg")
print("Вторая картинка")
cv2.imshow("window",img2)
cv2.waitKey(0)
if len(img2)>1000:
    print("Большая картинка")
else:
    print("Маленькая картинка")
#