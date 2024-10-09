import functools

ds = ['1111:271', '1111:190', '1231:106', '1211:104', '1111:201', '1231:120', '1001:205', '1001:223', '1001:127', '1001:236',
      '1111:229', '1231:286', '1231:195', '1001:279', '1001:124', '1111:292', '1505:219', '1231:259', '1231:253', '1001:220', '1001:202', '1231:103', '1211:249', '1212:275']
count = [111, 3, 13, 111, 9, 5, 17, 10, 13, 3, 16, 4, 16, 11, 18, 12, 14, 4, 3, 2, 14, 14, 10, 10]
#
# Из данных в списках создайте словарь `items_count`, в котором будет храниться количество товара на складе. Ключ — ID товара, значение — количество. Решение оформите в одну строчку.
new_dict = dict(zip(ds,count))
# 1. Количество уникальных категорий (решение оформите в одну строчку).// у нас явно не в одну )
obj = {}
for elem in ds:
      findId = elem.split(":")[0]
      if findId in obj:
            obj[findId]+=1
      else:
            obj[findId]=1
print(obj)
def filterID(number):

      return number[1]==1

new_obj = list(filter(filterID,obj.items()))
amount = len(new_obj)
print(amount)
# Среднее количество **уникальных товаров** в категории.

new_obj = list(sum(new_obj,()))
new_obj = [str(i) for i in new_obj]
findStr = ",".join(new_obj)
def filterAmount(elem):
      print(str(elem[0]).split(":")[0])
      return findStr.find(str(elem[0]).split(":")[0])>=0
new_dict =dict(filter(filterAmount,new_dict.items()))

print(new_dict)
buf = 0
for elem in new_dict.items():
      buf+=elem[1]
average = buf/amount
print(round(average,1))

#  ID товаров с максимальным количеством единиц на складе.
new_dict1 = dict(zip(ds,count))
for elem in new_dict1.items():
      if elem[1]==max(count):
            print(elem)

