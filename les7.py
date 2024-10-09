number = int(input("Enter any number"))
def check(num):
    strInfo = ""
    state = True
    if num%2==0:
        strInfo+="Четное,"
    if num>0:
        strInfo+="Положительное,"
    for i in range(2,(num//2)+1):
        if num%i == 0:
            state = False
            break
    if not state:
        strInfo+="Не является простым."
    else:
        strInfo += "Является простым."
    return strInfo



strInfo = check(number)
print(strInfo)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
