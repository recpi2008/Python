"""
Списки
Изменяемый тип

Операции:

append(элемент)
extend(список)
insert(позиция, элемент)
remove(элемент)
pop(позиция)
index(элемент)
count(элемент)
sort()
reverse()
copy()
clear()
enumerate(список)

strip()
"""

my_list = ['a', 'b', 'c', 'd', 'e', 'f']

my_list.append('j')  # добавляет элемент в конец списка
print(my_list)

my_list.extend(['h', 'i', 'g'])  # добавляет указанный список в конец исходного списка
print(my_list)

my_list.insert(3, 'w')  # вставляет указанный элемент на указанную позицию (индекс) в списке
print(my_list)

my_list.remove('w')  # удаляет элемент из списка. Упадет с ошибкой, если указанного элемента в списке нет.
print(my_list)

print(my_list.pop(4))  # удаляет элемент из списка. Вернет удаляемый элемент
print(my_list)

print(my_list.index('f'))  # возвращает индекс первого вхождения указанного элемента в списке

print(my_list[5])  # возвращает элемент списка в указанной позиции (индекс)

my_list.extend(['a', 'a', 'b', 'c', 'a'])

print(my_list.count('a'))  # считает количество элементов в списке

print(my_list[3:7])  # делает срез
print(my_list[2::3])

my_list.sort()  # производит сортировку списка
print(my_list)

print(list(reversed(my_list)))  # разворачивает список задом наперед

my_list_copy = my_list.copy()  # копирует список

my_list.clear()  # удаляет все элементы из списка
print(my_list)

print(list(enumerate(my_list_copy)))  # нумерует каждый элемент в списке. Возвращает кортеж из пар: (индекс, элемент)