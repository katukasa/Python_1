# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def sum_max(arg_1, arg_2, arg_3):
    try:
        my_list = [float(arg_1), float(arg_2), float(arg_3)]
        my_list.remove(min(my_list))
        return sum(my_list)
    except ValueError:
        return "Можно вводить только числа"


num_1 = input("Введите первое число: ")
num_2 = input("Введите второе число: ")
num_3 = input("Введите третье число: ")
print(sum_max(num_1, num_2, num_3))
