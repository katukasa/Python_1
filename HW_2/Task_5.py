# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

new_element = int(input("Введите рейтинг от 0 до 9: "))
my_list = [7, 5, 3, 3, 2]
my_list_len = len(my_list)
if new_element <= my_list[0]:
    index = my_list_len - 1
    while index < my_list_len:
        element = my_list[index]
        if new_element <= element:
            my_list.insert(index + 1, new_element)
            break
        index = index - 1
else:
    my_list.insert(0, new_element)
print(my_list)
