
from time import sleep

class TrafficLight:
    color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


a = TrafficLight()
a.running()


class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weight = 25
        self.heigth = 5


    def asphalt(self):
        asphalt = self.length * self.width * self.weight * self.heigth / 1000
        print(f"Для покрытия дороги необходимо {round(asphalt)} асфальта")

r = Road(4000, 100)
r.asphalt()



class Worker:


    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):


    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]

p = Position("Иван", "Иванов", "строитель", "100000", "20000")
print(p.get_full_name(), p.get_total_income())


class Car:

    def __init__(self, name, speed, color, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name + " Поехала")

    def stop(self):
        print(self.name + " Остановилась")

    def turn_right(self):
        print(self.name + " Повернула направо")

    def turn_left(self):
        print(self.name + " Повернула налево")

    def show_speed(self):
        print("Ваша скорость " + self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили скорость")
        else:
            print("Вы соблюдаете скоростной режим")

class SportCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили скорость")
        else:
            print("Вы соблюдаете скоростной режим")


class WorkCar(Car):
     def show_speed(self):
        if self.speed > 40:
            print("Вы превысили скорость")
        else:
            print("Вы соблюдаете скоростной режим")

class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили скорость. Но вы полиция вам можно)")
        else:
            print("Вы соблюдаете скоростной режим")


town = TownCar("Мерседес", 70, "Черный", False)
print(town.go(), town.stop(), town.turn_right(), town.turn_left(), town.show_speed())

sport = SportCar("Ауди", 45, "Синий", False)
print(sport.go(), sport.stop(), sport.turn_right(), sport.turn_left(), sport.show_speed())

work = WorkCar("Тойота", 120, "Белый", False)
print(work.go(), work.stop(), work.turn_right(), work.turn_left(), work.show_speed())

police = PoliceCar("БМВ", 90, "Бело-Синий", True)
print(police.go(), police.stop(), police.turn_right(), police.turn_left(), police.show_speed())


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")

pen = Pen("Ручка")
print(pen.draw())
pencil = Pencil("Карандаш")
print(pencil.draw())
handle = Handle("Маркер")
print(handle.draw())
