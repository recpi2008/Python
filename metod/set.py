"""
Множество

set() - изменяемый тип данных
frozenset() — неизменяемый

Операции:

add(элемент)
remove(элемент)
discard(элемент)
pop()
copy()
clear()

union(множество) ИЛИ |
intersection(множество) ИЛИ &
difference(множество) ИЛИ -
"""

my_set = set([1, 2, 3, 4, 5, 6, 7])
my_frozenset = frozenset([9, 8, 7, 6, 5])

my_set.add(8)  # добавляет 1 элемент во множество
print(my_set)

my_set.remove(5)  # удаляет указанный элемент из множества. Если такого элемента нет - завершается с ошибкой.
print(my_set)

my_set.discard(4)  # удаляет элемент из множества.
print(my_set)

my_set.discard(9)  # не сваливается с ошибкой, если такого элемента нет
print(my_set)

print(my_set.pop())  # удаляет первый элемент и возвращает значение удаляемого элемента

my_set_copy = my_set.copy()  # копирование множества

my_set.clear()  # обнуление

print(my_set_copy.union(my_frozenset))  # объединение множеств
print(my_set_copy.intersection(my_frozenset))  # пересечение множеств
print(my_set_copy.difference(my_frozenset))  # разница множеств
