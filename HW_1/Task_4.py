number = int(input("Введите целое положительное число: "))
max_num = 0
while number > 0:
    last = number % 10
    if last > max_num:
        max_num = last
        if max_num == 9:
            break
    number = number // 10
print(f"Наибольшая цифра в вашем числе равна {max_num}")
