callor = int(input("Введите калории, которые вы сегодня съели"))
norma_min = 2300
norma_max = 2600
if callor > norma_max:
    print("Вы съели очень много")
    print("1 - нужно сходить в туалет, 2 - выпьем угля, 3- попрыгать, чтобы улеглось")
    selection = int(input("Сделайте выбор: "))
    if selection == 1:
        print(" Идем в туалет")
    if selection == 2:
        print("Выпьем угля")
    if selection == 3:
        print(" прыгаем")
    if selection > 3 or selection < 1:
        print("Такого варианта нету, попробуйте ещё раз")
if callor < norma_min:
    print("Вы съели очень мало ")
    print("1 - Я съем банан, 2 - Сходить в KFC и съесть картошку фри, 3- съесть киреешки")
    selection = int(input("Сделайте выбор: "))
    if selection == 1: # Если
        print(" Кушаем банан")
    elif selection == 2: # Иначе если
        print("Идем в KFC")
    elif selection == 3: #Иначе если
        print(" Кушаем кереешки")
    else:# Иначе
        print("Такого варианта нету, попробуйте ещё раз")
if callor > norma_min and callor < norma_max:
    print("Вы съели ровно норму")
