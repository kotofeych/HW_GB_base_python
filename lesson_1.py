a1 = 1
b1 = 2
print(a1 + b1)

a2 = "1"
b2 = "2"
print(a2 + b2)

a3 = "1"
b3 = 2
print(type(a3), type(b3))

str1 = input("Введите строку 1: ")
str2 = input("Введите строку 2: ")
print(str(str1))
print(str(str2))

int1 = input("Введите число  1: ")
int2 = input("Введите число 2: ")
print(int(int1))
print(int(int2))

### ===========================================================

input_second = int(input("Введите время в секундах: "))

hour = input_second // 3600
minutes = (input_second - hour * 3600) // 60
seconds = input_second - (hour * 3600 + minutes * 60)

print(f"Введенное значение эквивалентно: {hour}:{minutes}:{seconds}")

### ===========================================================

input_number = int(input("Введите число : "))
summa = (
    input_number +
    int(str(input_number) + str(input_number)) +
    int(str(input_number) + str(input_number) + str(input_number))
)
print(summa)

### ===========================================================

input_max_number = abs(int(input("Введите целое, положительное число: ")))
modulo = input_max_number % 10

while input_max_number >= 1:
    input_max_number = input_max_number // 10

    if input_max_number % 10 > modulo:
        modulo = input_max_number % 10
    if input_max_number > 9:
        continue
    else:
        print("Самая большая цифра в числе ", modulo)
        break

### ===========================================================

profit = float(input("Введите доходы фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if profit > costs:
    print("Фирма имеет доход. Это хорошо.")
    print(f"Рентабильность конторы составляет: {profit / costs} %.")
    personal = int(input("Сколько сотруников работает у вас? "))
    print(f"Мы предполагаем, что на каждого сотрудника пришлось прибыли в размере: {profit / personal} .")
elif profit == costs:
    print("Фирма `стоит` на месте. Мы работаем в нолью.")
else:
    print("Убыточна фирма. Пора закрываться.")

### ===========================================================

day_a = int(input("Сколько киллометров вы пробежали? "))
day_b = int(input("Сколько вы хотели бы пробежать? "))
result_day = 1
result_km_day = day_a
result_km = day_a
while result_km < day_b:
    result_km_day = result_km_day + 0.1 * result_km_day
    result_day += 1
    result_km = result_km + result_km_day
print(f"Вам потребуется {result_day} дня(ей), чтобы пробежать {result_km} км.")

