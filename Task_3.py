# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open("task_3.txt", "r", encoding="utf-8") as my_file:
    names_list = []
    salary_list = []
    for line in my_file:
        line_list = line.split()
        names_list.append(line_list[0])
        salary_list.append(line_list[1])
        salary_list = list(map(lambda el: float(el), salary_list))

print("Сотрудники с окладом менее 20000:")
i = 0
while i < len(names_list):
    if float(salary_list[i]) < 20000:
        print(names_list[i], salary_list[i])
    i += 1

average_salary = sum(salary_list) / len(salary_list)
print("Средняя заработная плата:", average_salary)
