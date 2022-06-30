# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

def fact(num):
    try:
        num = int(num)
        if num < 0:
            print("Ошибка ввода")
        fact_num = 1
        for i in range(num + 1):
            yield f"{i}! = {fact_num}"
            fact_num *= i + 1
    except ValueError:
        print("Ошибка ввода")


input_num = input("Введите целое положительное число: ")

for step in fact(input_num):
    print(step)
