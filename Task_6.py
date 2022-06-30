# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.

from itertools import count, cycle

my_count = count(111, 111)
my_cycle = cycle("PYTHON")

for i in range(6):
    print(next(my_count), next(my_cycle))
