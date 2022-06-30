# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def mult_list(num_1, num_2):
    return num_1 * num_2


input_list = [i for i in range(100, 1001, 2)]
result = reduce(mult_list, input_list)

print(input_list)
print(result)
