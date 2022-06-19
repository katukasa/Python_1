# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

# через list
month = int(input("Введите номер месяца: "))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print("winter")
if month in spring:
    print("spring")
if month in summer:
    print("summer")
if month in autumn:
    print("autumn")

# через dict
month = int(input("Введите номер месяца: "))
winter = "winter"
spring = "spring"
summer = "summer"
autumn = "autumn"
year = {winter: [12, 1, 2], spring: [3, 4, 5], summer: [6, 7, 8], autumn: [9, 10, 11]}
if month in year.get(winter):
    print(winter)
if month in year.get(spring):
    print(spring)
if month in year.get(summer):
    print(summer)
if month in year.get(autumn):
    print(autumn)
