# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    __color = "red"

    def running(self):
        print(f"TrafficLight is on.")
        while True:
            if self.__color == "red":
                print(f"{self.__color}")
                sleep(7)
                self.__color = "yellow"
            if self.__color == "yellow":
                print(f"{self.__color}")
                sleep(2)
                self.__color = "green"
            if self.__color == "green":
                print(f"{self.__color}")
                sleep(5)
                self.__color = "red"


trafficLight = TrafficLight()
trafficLight.running()
