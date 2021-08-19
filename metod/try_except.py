try:
    print(500 / 0)
except ZeroDivisionError:
    print("Деление на ноль!")

my_dict = {'1': 1, '2': 2}
try:
    print(my_dict['3'])
except KeyError:
    print('Нет такого ключа!')


