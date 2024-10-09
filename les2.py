# import random
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 0, 7, 3, 2]
#
# def findIndexArray(arr):# найти номера тех элементов которые больше указанного числа
#     control_Number = int(input("Enter any number"))
#     empty = []
#     count = 0
#     for a in arr:
#         count += 1
#         if a > control_Number:
#             empty.append(count)
#     return empty
#
# def getSum(arr): #найти сумму от минимального элемента до максимального элемента
#     indexMax = arr.index(max(arr))
#     indexMin = arr.index(min(arr))
#     if indexMin < indexMax:
#         print(sum(arr[indexMin + 1:indexMax]))
#     else:
#         print("Невозможно найти сумму с таким расположением максимального и минимального числа")
#
#
# getSum(arr)
# matrix = [[random.randint(0, 10) for i in range(4)] for j in range(4)]
#
#
# def normaMatrix(matrix):# посчитать норму матрицы
#     print(sum(sum(matrix, [])))
#
#
# normaMatrix(matrix=matrix)
import urllib3
import urllib.error
import urllib.request
response = urllib.request.urlopen("https://itproger.com/course/java-spring/3")
print(response.read())

import urllib.parse

urlParse = urllib.parse.urlparse("https://itproger.com/course/java-spring/3")
print(urlParse)
urlUnparse = urllib.parse.urlunparse(urlParse)
print(urlUnparse)
urlSplit = urllib.parse.urlsplit("https://itproger.com/course/java-spring/3")
print(urlSplit)
urlUnsplit = urllib.parse.urlunsplit(urlSplit)
print(urlUnsplit)


urlResponse = urllib.request.urlopen("https://itproger.com/course/java-spring/3")
print(urlResponse)
print(urlResponse.info())
print(urlResponse.info()["Server"])
print(urlResponse.info()["Date"])
print(urlResponse.info()["Content-Type"])
response  = urllib.request.urlopen("http://127.0.0.1:5500/Untitled-1.html")
print(response.geturl())
for line in response:
    print(line)
try:
    url = input("Введите любой адрес URL: ")
    response = urllib.request.urlopen(url)
    print(response.read())
except urllib.error.URLError as e:
    print("Ошибка URL")
except ValueError:
    print("Введит действительный адрес")