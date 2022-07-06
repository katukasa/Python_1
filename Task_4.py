# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

from random import choice


class Car:
    direction = ["left", "right"]

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"Go-go {self.name} car!")

    def stop(self):
        print(f"{self.name} car stopped.")

    def turn(self):
        print(f"{self.name} car turned {choice(self.direction)}.")

    def show_speed(self):
        print(f"{self.name} car has speed {self.speed} km/h.")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name} car exceeded the speed limit 60 km/h!")


class SportCar(Car):
    """ no changes """


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name} car exceeded the speed limit 40 km/h!")


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)


town_car = TownCar("Lada", "blue", 80)
sport_car = SportCar("Ferrari", "red", 200)
work_car = WorkCar("Kamaz", "yellow", 45)
police_car = PoliceCar("VAZ", "white", 90)

cars = [town_car, sport_car, work_car, police_car]

for car in cars:
    car.go()
    car.turn()
    car.show_speed()
    car.stop()
    print()
