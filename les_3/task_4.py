"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения
числа в степень.
"""
x = int(input("Введите первое положительное число: "))
y = int(input("Введите второе отрицательное число: "))
def my_func(x, y):
    n = 1
    temp = x
    y = y * (-1)
    while n < y:
        x = x * temp
        n = n + 1
    return x
result = my_func(x, y)
print(result)