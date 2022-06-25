# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def user_info(name, surname, birth_year, city, e_mail, phone_number):
    return f"{name} {surname} {birth_year} {city} {e_mail} {phone_number}"


print(user_info(name="Василий", surname="Пупкин", birth_year="1980",
                city="Москва", e_mail="bla-bla@mail.ru", phone_number="+7123456789"))
