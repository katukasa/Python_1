# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open("task_2.txt", "r", encoding="utf-8") as my_file:
    line_num = 0
    for line in my_file:
        line_num += 1
        print(f"{line_num} line -", end=" ")
        line_list = line.split()
        print(f"{len(line_list)} words")
    print(f"Amount of lines: {line_num}")
