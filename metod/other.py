"""
Тернарный оператор
"""

result = True if 5 > 4 else False
print(result)

condition = False
personality = ("не проверено", "проверено")[condition]
print(personality)

"""
is - сравнение по ссылке (сравнение на идентичность объектов)
in - проверка на вхождение элемента в контейнер данных
"""

my_list = [1]
print(my_list == [1])
print(my_list is [1])

print(None == None)
print(None is None)

print('Саша' in 'Шла Саша по шоссе')
print(1 in [8, 7, 6, 5, 4, 3, 2, 1])

"""
пустые структуры данных являются Falsy
"""

my_empty_list = []
my_empty_string = ""
my_empty_dict = {}
my_empty_tule = ()

if my_empty_list:
    print('Структура не пуста')
else:
    print('Структура пуста')

"""
пересваивание значений переменных
"""

a = 42
b = 'my_string'

a, b = b, a
print("a:", a, " ", "b:", b)