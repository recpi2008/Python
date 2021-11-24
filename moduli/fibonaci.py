"""
Последовательность Фибоначчи
1 2 3 5 8 13 21 34 55 89 ...
"""

def fibonacci(xterms):
    # первые два условия
    x1 = 0
    x2 = 1
    count = 0

    if xterms <= 0:
        print("Укажите целое число больше 0")
    elif xterms == 1:
        print("Последовательность Фибоначчи до", xterms, ":")
        print(x1)
    else:
        while count < xterms:
            xth = x1 + x2
            x1 = x2
            x2 = xth
            count += 1
            yield xth

fib = fibonacci(5)

for element in fibonacci(10):
    print(element)

# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
