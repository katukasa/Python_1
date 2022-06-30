# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary():
    try:
        name, hours, cost, prem = argv
        hours = float(hours)
        cost = float(cost)
        prem = float(prem)
        result = (hours * cost) + prem
        print(f"Выработка в часах: {hours}, ставка в час: {cost}, премия: {prem}")
        print(f"Зарплата: {result}")
    except ValueError:
        print("Ошибка в данных")


salary()
