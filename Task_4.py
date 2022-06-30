# 4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

from random import randint

input_list = [randint(1, 35) for num in range(25)]
new_list = []
for i in input_list:
    if input_list.count(i) == 1:
        new_list.append(i)


print(input_list)
print(new_list)


# переделано со словарем

input_list = [randint(1, 35) for num in range(25)]
work_dict = {i: 0 for i in input_list}

for i in input_list:
    work_dict[i] += 1

new_list = [i for i in work_dict if work_dict[i] == 1]

print(input_list)
print(new_list)
