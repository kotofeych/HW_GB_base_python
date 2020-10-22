########## Ex.1
list_type_vars = list()
list_type_vars.append(int(4))
list_type_vars.append(str("Hi"))
list_type_vars.append(float(1.2))
list_type_vars.append(dict(qw = '1', qw2 = '2'))
list_type_vars.append(tuple("2"))
list_type_vars.append(bool(True))
list_type_vars.append(b"Hello")
list_type_vars.append(None)
print(list_type_vars)
for i in list_type_vars:
    if type(i) == int:
        print(str(i) + " - Это числовое значение!")
    elif type(i) == str:
        print(str(i) + " - Это строковое значение!")
    elif type(i) == float:
        print(str(i) + " - Это число с запятой!")
    elif type(i) == dict:
        print(str(i) + " - Это значение принадлежит к типу 'словарь'!")
    elif type(i) == tuple:
        print(str(i) + " - Это значение принадлежит к типу 'кортеж'!")
    elif type(i) == bool:
        print(str(i) + " - Это значение принадлежит к типу 'bool'!")
    elif type(i) == bytes:
        print(str(i) + " - Это значение принадлежит к типу 'bytes'!")
    elif i is None:
        print(str(i) + "Тип 'None' ни чего в себе не несет, т.к. это пустота!")

########## Ex.2
volume = int(input("Сколько будет элиментов? "))
input_list = []
i = 0
col = 0


while i < volume:
    input_list.append(input("Введите очередной элемент для списка: "))
    i += 1

print("Ок. Вы ввели желаемое количество элементов. Идем дальше, и давайте посмотрим на перемещенный список.")

for ii in range(int(len(input_list)/2)):
    input_list[col], input_list[col+1] = input_list[col+1], input_list[col]
    col += 2

print(input_list)

########## Ex.3
month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь', ]
season_list = ['зима', 'весна', 'лето', 'осень', ]
month_dict = {
    "1": 'январь',
    "2": 'февраль',
    "3": 'март',
    "4": 'апрель',
    "5": 'май',
    "6": 'июнь',
    "7": 'июль',
    "8": 'август',
    "9": 'сентябрь',
    "10": 'октябрь',
    "11": 'ноябрь',
    "12": 'декабрь'
}
season_dict = {
    1: 'зима',
    2: 'весна',
    3: 'лето',
    4: 'осень'
}

number_check_dict = int(input("Введите число, сколько раз вы хотите проверить правильность задания? "))
number = 0
number_month = 0

while number < number_check_dict:
    number += 1
    number_month = int(input("Введите порядковый номер интересующего вас месяца: "))

    if number_month < 0 or number_month > 12:
        print("Не правильно указан номер месяца.")
        exit()

    for month_key, month_value in month_dict.items():

        if int(month_key) == int(number_month):
            print("Dict. Вы указали месяц - " + month_value)
            print("List. Вы указали месяц - " + month_list[int(number_month)-1])

            if int(month_key) >= 3 and int(month_key) <= 5:
                print("Dict. Указанный месяц соответствует сезону - " + season_dict.get(2))
                print("List. Указанный месяц соответствует сезону - " + season_list[1])
            elif int(month_key) >= 6 and int(month_key) <= 8:
                print("Dict. Указанный месяц соответствует сезону - " + season_dict.get(3))
                print("List. Указанный месяц соответствует сезону - " + season_list[2])
            elif int(month_key) >= 9 and int(month_key) <= 11:
                print("Dict. Указанный месяц соответствует сезону - " + season_dict.get(4))
                print("List. Указанный месяц соответствует сезону - " + season_list[3])
            elif int(month_key) >= 12 or int(month_key) <= 2:
                print("Dict. Указанный месяц соответствует сезону - " + season_dict.get(1))
                print("List. Указанный месяц соответствует сезону - " + season_list[0])


########## Ex.4
string_input = input("Введите ваше предложение: ")
string_unsplit = []
number = 1
for i in range(string_input.count(' ') + 1):
    string_unsplit = string_input.split()
    if len(str(string_unsplit)) <= 10:
        print(f" {number} {string_unsplit [i]}")
        number += 1
    else:
        print(f" {number} {string_unsplit [i] [0:10]}")
        number += 1

########## Ex.5
rating = [7, 5, 3, 3, 2]
print(f"Рейтинг - {rating}")
input_rating = int(input("Для выхода, введите число 911. "))
while input_rating != 911:
    for i in range(len(rating)):
        if rating[i] == input_rating:
            rating.insert(i + 1, input_rating)
            break
        elif rating[0] < input_rating:
            rating.insert(0, input_rating)
        elif rating[-1] > input_rating:
            rating.append(input_rating)
        elif rating[i] > input_rating and rating[i + 1] < input_rating:
            rating.insert(i + 1, input_rating)
    print(f"текущий список - {rating}")
    input_rating = int(input("Введите число "))
