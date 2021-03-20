"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Ряд строить программно - в самой же рекурсивной ф-ции
или даже обойтисть без создания ряда

Элемент в 2 раза меньше предыд и имеет противопол знак
"""


def my_sum(num, x=1., x_sum=0):
    if num < 1:
        return 0
    x_sum += x
    if num == 1:
        return x_sum
    else:
        return my_sum(num-1, x/-2, x_sum)


print(my_sum(int(input('Please enter a positive integer: '))))
