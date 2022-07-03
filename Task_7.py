# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет
# содержать данные о фирме: название, форма собственности, выручка, издержки.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open("task_7.txt", "r", encoding="utf-8") as my_file:
    firms = []
    profits = []
    for line in my_file:
        line_list = line.split()
        firms.append(line_list[0])
        profits.append(int(line_list[2]) - int(line_list[3]))

i = 0
sum_profits = 0
num_with_profit = 0
while i < len(profits):
    if profits[i] > 0:
        sum_profits += profits[i]
        num_with_profit += 1
    i += 1

to_json = [dict(zip(firms, profits)), dict(average_profit=sum_profits / num_with_profit)]

with open("task_7_temp.json", "w", encoding="utf-8") as write_file:
    json.dump(to_json, write_file, ensure_ascii=False, indent=4)
