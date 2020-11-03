# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
class TrafficLight:
    # 7 + 2 + 6
    try:
        i_rate = int(input("How many reps? (One cycle - 15 sec. Cycle can't be more than 30 ): ->>> "))
        if i_rate > 30:
            raise BaseException
    except BaseException:
        print("Error. Please, enter to int number.")
        exit(-1)

    __color = ('red', 'yellow', 'green')

    def running(self):
        i_cycle = 0

        while i_cycle < self.i_rate:
            i_cycle += 1
            i_text = "The traffic light is now on:"

            for i_color in TrafficLight.__color:
                if i_color == 'red':
                    print(i_text, i_color)
                    sleep(7)
                elif i_color == 'yellow':
                    print(i_text, i_color)
                    sleep(2)
                elif i_color == 'green':
                    print(i_text, i_color)
                    sleep(6)
                else:
                    print("Error. Please restart program.")
                    exit(-1)

TrafficLight().running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
#       длина * ширина
#           * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
#           * число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def square(self):
        return self._length * self._width
        # depth, heft


class MassAsphalt(Road):
    pass


i_vars = MassAsphalt(20, 5000).square()
print(i_vars)


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, i_wage, i_bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": i_wage, "bonus": i_bonus}


class Position(Worker):

    def __init__(name, surname, position, i_wage, i_bonus):
        super().__init__(name, surname, position, i_wage, i_bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


i_position = Position('Basil', 'Basil', 'manager', 5000, 10000)
print(i_position.get_full_name())
print(i_position.get_total_income())
print(i_position.name)
print(i_position.surname)
print(i_position.position)
print(i_position._income)


# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
class Car:

    def __init__(self, speed, color, name, is_police):
        try:
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = bool(is_police)
            # if (not self.speed or len(self.speed) <= 0) or \
            #         (not self.color or len(self.color) <= 0) or \
            #         (not self.name or len(self.name) <= 0) or \
            #         not bool(self.is_police):
            #     raise BaseException
        except BaseException:
            return "Error. Please, enter data."
            exit(-1)

    def go(self):
        return "Go."

    def stop(self):
        return "Stop."

    def turn_left(self):
        return "Turn left."

    def turn_right(self):
        return "Turn right."

    def show_speed(self):
        print("Machine normal speed.")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Over speed."
        else:
            return "Normal speed"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Over speed."
        else:
            return "Normal speed"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


toyota = SportCar(100, 'Red', 'Toyota', False)
mazda = TownCar(30, 'White', 'Mazda', True)
suzuki = WorkCar(70, 'Rose', 'Suzuki', False)
honda = PoliceCar(110, 'Blue',  'honda', True)


print(toyota.turn_left())
print(mazda.turn_right())
print(suzuki.stop())
print(honda.go())
print(suzuki.is_police)
print(honda.is_police)
print(suzuki.show_speed())
print(honda.show_speed())



# 5. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
# ?
# ?
# ?
# ?


# 6. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start rendering.")


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Uses Pen"


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Uses Pencil"


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Uses Handle"


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
