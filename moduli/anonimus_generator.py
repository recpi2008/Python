"""
List comprehension vs generator
"""

# Создаем список
alist = [4, 16, 64, 256]

# Вычислим квадратный корень, используя генерацию списка
out = [a**(1/2) for a in alist if a == 4]
print(out)

out = [a**(1/2) if a == 4 else None for a in alist]
print(out)

# Используем выражение генератора, чтобы вычислить квадратный корень
out = (a**(1/2) for a in alist)
print(out)
print(next(out))
print(next(out))
print(next(out))
print(next(out))
#
# # Создание словарей
my_dict = {el: el*2 for el in range(10, 20)}
print(my_dict)
#
# # Создание множеств
my_set = {el**3 for el in range(5, 10)}
print(my_set)