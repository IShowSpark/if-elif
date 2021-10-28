def again():
    print("")
    print("Пожалуйста, проверь свой месяц")
    print("Месяц должен быть следующим:")
    print("01 - Январь")
    print("02 - Февраль")
    print("03 - Март")
    print("04 - Апрель")
    print("05 - Май")
    print("06 - Июнь")
    print("07 - Июль")
    print("08 - Август")
    print("09 - Сентябрь")
    print("10 - Октябрь")
    print("11 - Ноябрь")
    print("12 - Декабрь")
    print("")
def zodiac():
    month = input("Месяц рождения =>")
    day = int(input("День рождения =>"))
    bday = ( month + "/" + str(day))
    if (int(month) > 12):
        again()
        zodiac()
    elif month == "01":
        if (day > 31):
            print("")
            print("Неверная дата!")
            print("Попробуйте заново!")
            print("")
            zodiac()            
        elif (day <= 20):
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Скорпион!")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Водолей")
    elif month == "02":
        if (day >28):
            print("")
            print("Неверная дата!")
            print("Попробуйте заново!")
            print("")
            zodiac()
        elif (day <= 18):
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Водолей")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Рыба")
    elif month == "03":
        if (day > 31):
            print("")
            print("Неверная дата!")
            print("Попробуйте заново!")
            print("")
            zodiac()
        elif (day <= 20):
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Рыба")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Овен")
    elif month == "04":
        if (day > 30):
            print("")
            print("Неверная дата!")
            print("Попробуйте заново!")
            print("")
            zodiac()
        elif (day <= 20):
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Овен")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Телец")
    elif month == "05":
        if (day > 31):
            print("")
            print("Неверная дата!")
            print("Попробуйте заново!")
            print("")
            zodiac()
        elif (day <= 20):
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Телец")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будетs Близнецы")
    elif month == "06":
        if (day > 30):
            print("")
            print("Неверная дата!")
            print("Повторите заново!")
            print("")
            zodiac()
        elif (day <= 21):
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Близнецы")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Рак")
    elif month == "07":
        if (day > 31):
            print("")
            print("Неверная дата!")
            print("Повторите заново!")
            print("")
            zodiac()
        elif (day <= 22):
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Рак")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Лев")
    elif month == "08":
        if (day > 31):
            print("")
            print("Неверная дата!")
            print("Повторите заново!")
            print("")
            zodiac()
        elif (day <=23):
            print("Твой день рождения=>",bday)
            print("Тогда твой знак зодиака будет Лев")
        else:
            print("Твой день рождения=>",bday)
            print("Тогда твой знак зодиака будет Дева")
    elif month == "09":
        if (day > 30):
            print("")
            print("Неверная дата!")
            print("Повторите заново!")
            print("")
            zodiac()
        elif (day <= 23):
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Дева")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Весы")
    elif month == "10":
        if (day > 31):
            print("")
            print("Неверная дата!")
            print("Повторите заново!")
            print("")
            zodiac()
        elif (day <= 23):
            print("Твой день рождения=>",bday)
            print("Тогда твой знак зодиака будет Весы")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Скорпион")
    elif month == "11":
        if (day > 30):
            print("")
            print("Неверная дата!")
            print("Повторите заново!")
            print("")
            zodiac()
        elif (day <= 23):
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Скорпион")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Стрелец")
    elif month == "12":
        if (day > 31):
            print("")
            print("Неверная дата!")
            print("Повторите заново!")
            print("")
            zodiac()
        elif (day <= 21):
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Стрелец")
        else:
            print("Твой день рождения =>",bday)
            print("Тогда твой знак зодиака будет Козерог")
    else:
        print("")
        again()
        zodiac()
zodiac()
print("")
again = input("Введи 'zodiac' если хочешь повторить процедуру => ")
if (again == "zodiac"):
    zodiac()

