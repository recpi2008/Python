from functools import reduce, partial

"""
сборник функций высокого уровня:
взаимодействующих с другими функциями или возвращающие другие функции.

reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) вычисляет ((((1+2)+3)+4)+5)
"""


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el


print(reduce(my_func, [10, 20, 30]))


def my_func_2(param_1, param_2):
    return param_1 ** param_2


new_my_func = partial(my_func_2, 2)
print(new_my_func)
print(new_my_func(4))