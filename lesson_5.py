# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# file_open = open('1.txt', 'w')
# while True:
#     text_line = str(input("Input text line: \n"))
#     if text_line == "print":
#         file_open = open('1.txt', 'r')
#         print("\nPrint file:\n----------\n" + file_open.read() + "---------- \nEnd file.")
#         break
#     elif not text_line:
#         print("Exit.\n")
#         break
#     elif text_line:
#         file_open.write(text_line + "\n")
# file_open.close()

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

## create dynamic file
# def generator_file():
#     f_file_open = open('2.txt', 'w')
#     data_list = [
#                 'This', 'method', 'is', 'supplied', 'with', 'the', 'MersenneTwister', 'generator',
#                 'and', 'some', 'other', 'generators', 'may', 'also', 'provide',
#                 'it', 'as', 'an', 'optional', 'part', 'of', 'the', 'API2'
#                 ]
#     data = [
#         f_file_open.write(str(data_list[i]) + "\n") for i in range(len(data_list))
#     ]
#     f_file_open.close()
# generator_file()
#
# def count():
#     file_open = open('2.txt', 'r')
#     print("Count strings: " + str(len(file_open.readlines())) + ".")
#     file_open = open('2.txt', 'r')
#     print("Count elements: " + str(len(file_open.read())) + ".")
#
# count()

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32
#
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
def generator_file3():
    f_file_open = open('3_1.txt', 'w')
    data_list = [
                'Иванов 23543.12',
                'Петров 16659.74',
                'Сидоров 14568.32',
                'Ацтек 24573.75',
                'Фарнух 19159.64',
                'Кузнецов 19359.95',
                'Попов 34956.96',
                'Соколов 68425.73',
                'Михайлов 15457.29',
                'Котов 39856.48',
                ]
    data = [
        f_file_open.write(str(data_list[i]) + "\n") for i in range(len(data_list))
    ]
    f_file_open.close()


generator_file3()


def check_salary():
    f_file_open = open('3_1.txt', 'r')
    data = f_file_open.read()
    data_list = data.strip().split('\n')
    data_dict = {
        data_list[list_i].split()[el] : data_list[list_i].split()[el+1]
        for list_i in range(len(data_list))
        for el in range(len(str(list_i).split()))
    }
    list_person = []
    for i in range(len(data_dict.items())):
        # if float(data_dict.values()[i]) > 20000.00:
        list_person.append(data_dict.values()[23543.12])
    #     # if float(data_dict[i+1]) < 20000.00:
    #     list_person.append(data_dict[str(i)])

    return list_person


print(check_salary())





# rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# new_file = []
# with open('file_4.txt', 'r') as file_obj:
#     #content = file_obj.read().split('\n')
#     for i in file_obj:
#         i = i.split(' ', 1)
#         new_file.append(rus[i[0]] + '  ' + i[1])
#     print(new_file)
#
# with open('file_4_new.txt', 'w') as file_obj_2:
#     file_obj_2.writelines(new_file)



# 4. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# def summary():
#     try:
#         with open('file_5.txt', 'w+') as file_obj:
#             line = input('Введите цифры через пробел \n')
#             file_obj.writelines(line)
#             my_numb = line.split()
#
#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Ошибка в файле')
#     except ValueError:
#         print('Неправильно набран номер. Ошибка ввода-вывода')
# summary()

# 5. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# subj = {}
# with open('file_6.txt', 'r') as init_f:
#     for line in init_f:
#         subject, lecture, practice, lab = line.split()
#         subj[subject] = int(lecture) + int(practice) + int(lab)
#     print(f'Общее количество часов по предмету - \n {subj}')

# 6. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

# import json
# profit = {}
# pr = {}
# prof = 0
# prof_aver = 0
# i = 0
# with open('file_7.txt', 'r') as file:
#     for line in file:
#         name, firm, earning, damage = line.split()
#         profit[name] = int(earning) - int(damage)
#         if profit.setdefault(name) >= 0:
#             prof = prof + profit.setdefault(name)
#             i += 1
#     if i != 0:
#         prof_aver = prof / i
#         print(f'Прибыль средняя - {prof_aver:.2f}')
#     else:
#         print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
#     pr = {'средняя прибыль': round(prof_aver)}
#     profit.update(pr)
#     print(f'Прибыль каждой компании - {profit}')
#
# with open('file_7.json', 'w') as write_js:
#     json.dump(profit, write_js)
#
#     js_str = json.dumps(profit)
#     print(f'Создан файл с расширением json со следующим содержимым: \n '
#           f' {js_str}')
