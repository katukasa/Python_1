# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.

from random import randint

input_list = [randint(1, 100) for num in range(0, randint(10, 20))]
new_list = []
for i in range(1, len(input_list)):
    if input_list[i] > input_list[i - 1]:
        new_list.append(input_list[i])


print(input_list)
print(new_list)
