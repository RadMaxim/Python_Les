# power_2_numbers = []
# a,i= 2,1
# while pow(a,i)<200:
#     power_2_numbers.append(pow(a,i))
#     i+=1
# power_2_numbers = set(power_2_numbers)
# generated_set = []
# for i in range(8,51):
#     if i%5!=0:
#         generated_set.append(i)
#     else:
#         generated_set.append(1)
# generated_set = set(generated_set)
# print(power_2_numbers)
# print(generated_set)
# new_set = power_2_numbers.symmetric_difference(generated_set)
# print(new_set)
# new_set = list(filter(lambda item:34<item<120,new_set))
# print(new_set)
# unicode_values = {}
# for i in new_set:
#     unicode_values[i]=chr(i)
# print(unicode_values)
#
# //////////////////////////////////////////////////////
#
#
shedule = {
    '1001': ['пн', 'вс'],
    '1231': ['пн', 'вт'],
    '1232': ['ср', 'чт', 'пт'],
    '1280': ['ср', 'пт', 'вс'],
    '1282': ['чт'],
    '1290': ['пт', 'вс'],
    '1303': ['вт', 'вс'],
}
unique_days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
newShedule =set(sum(shedule.values(),[])).symmetric_difference( set(unique_days))
# print(newShedule)
allDay = sum(shedule.values(),[])
obj = {}
for a in allDay:
    if a in obj:
        obj[a]+=1
    else:
        obj[a]=1
print(obj)

