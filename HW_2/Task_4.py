# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

input_string = input("Введите несколько слов, разделенных пробелами: ")
new_list = input_string.split()
new_list_len = len(new_list)
index = 0
while index < new_list_len:
    print(f"{index + 1}: {new_list[index][:10]}")
    index = index + 1
