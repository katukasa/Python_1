# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ["sky", -6, ["meaning", 42], 5.5, True]
my_list_len = len(my_list)
index = 0
while index < my_list_len:
    print(my_list[index], "-", type(my_list[index]))
    index += 1
