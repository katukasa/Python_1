# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 # Two — 2 # Three — 3 # Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator

with open("task_4_temp.txt", "w", encoding="utf-8") as output_file:
    with open("task_4.txt", "r", encoding="utf-8") as input_file:
        text_to_translate = input_file.read()
    try:
        output_file.write(Translator().translate(text_to_translate, dest="ru").text)
    except AttributeError:
        print("Не так часто :)")
