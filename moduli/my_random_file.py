"""
Встроенный модуль random

randint(<Начало>, <Конец>)
choice(<Последовательность>)
randrange(<Начало>, <Конец>, <Шаг>)
shuffle(<Последовательность>)
choice(<Последовательность>)
sample(<Последовательность>, кол-во элементов)
gauss(<Начало>, <Конец>)
"""

import random
print(random.randint(3, 9))
print(random.randrange(3, 13, 2))
print(random.random()*10)
a = [1, 2, 3, 4, 5, 6, 7]
print(random.choice(a))
print(random.sample(a, 3))
random.shuffle(a)
print(a)
print(random.gauss(0, 1))

