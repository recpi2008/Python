"""
Генераторы
"""

# print(range(7))
# print(list(range(2, 8)))


def gen():
    x = 42
    yield x
    x += 1
    yield x
    x += 1
    yield x

g = gen()
print(g)
print(next(g))
print(next(g))
print(next(g))

for i in gen():
    print(i)
