def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# gen = infinite_sequence()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))



def two_powerful(number):
    for power in range(number):
        yield 2 ** power

gen = two_powerful(6)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))