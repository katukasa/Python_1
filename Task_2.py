# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_count(self):
        pass


class Coat(Clothes):
    @property
    def fabric_count(self):
        return round((self.param / 6.5) + 0.5, 2)


class Suit(Clothes):
    @property
    def fabric_count(self):
        return round(((self.param / 100) * 2) + 0.3, 2)


coat = Coat(38)
print(coat.fabric_count)

suit = Suit(175)
print(suit.fabric_count)

print(round(coat.fabric_count + suit.fabric_count, 2))
