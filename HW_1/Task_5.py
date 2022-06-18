revenue = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
if cost > revenue:
    print("Фирма работает в убыток")
if cost == revenue:
    print("Выручка фирмы равна издержкам")
if cost < revenue:
    print("Фирма работает с прибылью")
    profit = revenue - cost
    profitability = profit / revenue
    print("Рентабельность фирмы:", profitability)
    employees = int(input("Введите количество сотрудников в фирме: "))
    profit1 = profit / employees
    print("Прибыль фирмы в расчёте на одного сотрудника равна", profit1)
