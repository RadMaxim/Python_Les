complaint_stat = [
    [27, 22, 15, 8, 3, 16, 15],
    [12, 4, 10, 13, 29, 22, 121],
    [5, 7, 6, 13, 2, 1, 25],
    [15, 6, 14, 19, 25, 7, 3]
]


def get_average_number(list):
    arr = sum(list, [])
    sumAll = sum(arr)
    find_average = sumAll / len(arr)
    return arr,int(find_average)


def outlier_days_count():
    count_days = 0
    arr,average_number = get_average_number(complaint_stat)
    print("Среднее колличество жалоб - "+ str(average_number))
    for days in arr:
        if days > average_number:
            count_days+=1
    print("Колличество дней с повышенным колличеством жалоб - "+count_days.__str__())
    return average_number,count_days
def get_complaint_info_Weeks(weeks):
    sumWeek = sum(weeks)
    aver = int(sumWeek/len(weeks))
    countDay = 0
    for day in weeks:
        if day>aver:
            countDay+=1
    return countDay,aver
def get_complaint_info(weeks):
    countWeeks = 0
    for week in weeks:
        countDay,aver = get_complaint_info_Weeks(week)
        countWeeks+=1
        print("Неделя "+str(countWeeks)+"  "+str(week)+" повышенные дни - "+str(countDay)+" Среднее колличество жалоб -  "+str(aver))


get_complaint_info(complaint_stat)


