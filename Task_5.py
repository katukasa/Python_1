# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

list_1 = [randint(1, 100) for num in range(0, randint(10, 20))]
str_1 = ' '.join(map(lambda el: str(el), list_1))

with open("task_5_temp.txt", "w", encoding="utf-8") as file_1:
    file_1.write(str_1)

with open("task_5_temp.txt", "r", encoding="utf-8") as file_2:
    str_2 = file_2.read()
    list_2 = list(map(lambda el: int(el), str_2.split()))
    sum_res = sum(list_2)

print(str_1)
print(str_2)
print(sum_res)
