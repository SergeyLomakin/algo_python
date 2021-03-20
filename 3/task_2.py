"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
import hashlib
from uuid import uuid4


def check_pas():
    salt = uuid4().hex

    user_password_input_one = input('Please, input your password: ')
    pas_one = hashlib.sha256(salt.encode() + user_password_input_one.encode()).hexdigest()

    user_password_input_two = input('Please, input your password again: ')
    pas_two = hashlib.sha256(salt.encode() + user_password_input_two.encode()).hexdigest()

    if pas_two == pas_one:
        return print('You entered the correct password')
    return print('wrong password')


check_pas()
