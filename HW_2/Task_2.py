# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list = []
amount = int(input("Сколько элементов вы хотите ввести? "))
while amount > 0:
    my_list.append(input("Введите элемент: "))
    amount = amount - 1
print(my_list)

amount = len(my_list)
index_1 = 0
index_2 = 1
if amount < 2:
    print("Недостаточно элементов для перестановки")
else:
    while index_2 < amount:
        element_1 = my_list[index_1]
        element_2 = my_list[index_2]
        my_list.pop(index_1)
        my_list.pop(index_1)
        my_list.insert(index_1, element_2)
        my_list.insert(index_2, element_1)
        index_1 = index_1 + 2
        index_2 = index_1 + 1
    print(my_list)
