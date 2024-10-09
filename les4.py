myData = "Фамилия:Радчук,Имя:Максим"
def get_name_data_first(data):
    secondName = data.split(",")[0].split(":")[1]
    firstName = data.split(",")[1].split(":")[1]
    return (secondName.lower(),firstName.lower())



print(get_name_data_first(myData))
def get_name_data(data,select):
    itog = ""
    secondName,firstName = get_name_data_first(data)
    if select=="Фамилия":
        itog=secondName
    if select=="Имя":
        itog=firstName
    return itog.lower()


print(get_name_data(myData,"Имя"))
user_cities = ['гМосква', 'КАЗАНЬ', 'Сочи', 'город сочи', 'г.казань.', 'СОЧИ ГОРОД', 'город солнца сочи', 'москва', 'СоЧИ', 'городказань ', 'Москва', 'город москва']
normalized_cities = ['москва', 'сочи', 'казань']
def city_norma(cityString,cityName,correct):

    normaString = cityString.lower()
    for i in cityName:
        print(i)
        if normaString.find(i)>=0:

            correct.append(i)
            break


def norma(user_cities,normalized_cities):
    correct = []
    print(user_cities)
    for i in user_cities:
        city_norma(i,normalized_cities,correct)
    for a,b in zip(correct,user_cities):
        print("До: "+str(b)+", После: "+str(a))
password = "abA7"
def check_pass(passord):
    wrong = ""
    check = True

    count=0
    count1=0
    if len(passord)<8:
        check = False
        wrong+="Этот пароль меньше 8 символов. "

    for i in passord:
        if i.isdigit():
            count+=1
        if i.isupper():
            count1+=1
    if passord.find("+")!=-1 or passord.find("$")!=-1:
        wrong+="В пароле не должны содержаться символы + и $. "
        check=False

    if count<2:
        check=False
        wrong+="В пароле должно быть хотя бы 2 цифры. "
    if count1==0:
        check = False
        wrong+="В пароле должна быть хотя б одна буквы верхнего регистра. "
    return "Ok" if check == True else wrong




print(check_pass(password))




# norma(user_cities,normalized_cities)
