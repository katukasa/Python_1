# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.

# в одну строку
my_list = [num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0]
print(my_list)

# первый вариант - не в одну стоку :)
first_list = list(range(20, 241))
second_list = []
for num in first_list:
    if num % 20 == 0 or num % 21 == 0:
        second_list.append(num)
print(first_list)
print(second_list)
