# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

with open("task_6.txt", "r", encoding="utf-8") as my_file:
    names = []
    hours = []
    for line in my_file:
        line_list = line.split(':')
        names.append(line_list[0])
        hours_list = map(int, "".join([el for el in line_list[1] if el == ' ' or '0' <= el <= '9']).split())
        hours.append(sum(hours_list))

print(dict(zip(names, hours)))
