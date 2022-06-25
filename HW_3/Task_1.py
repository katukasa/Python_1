# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(arg_1, arg_2):
    try:
        result = round((float(arg_1) / float(arg_2)), 4)
    except ValueError:
        return "Ошибка ввода: работаем только с числами"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return result


num_1 = input("Введите первое число: ")
num_2 = input("Введите второе число: ")
print(div(num_1, num_2))
