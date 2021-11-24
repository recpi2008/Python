import itertools
"""
count(start=0, step=1) - возвращает равномерно распределенные переменные
chain - конкатенирует произовльное число итераторов
"""

for i in itertools.count(10, 2):
    print(i)


# for i in itertools.cycle("ABC"):
#     print(i)

# a = itertools.chain(range(2), range(4, 8))
# for i in a:
#     print(i)

# Декартово произведение
# print(list(itertools.product("ABCD", repeat=2)))

# Перестановки
# print(list(itertools.permutations("ABС")))

# Сочетания
# print(list(itertools.permutations("ABCDE", 3)))

# Зацикливание
# progr_lang = ["python", "java", "perl", "javascript"]
# iter = itertools.cycle(progr_lang)
#
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
