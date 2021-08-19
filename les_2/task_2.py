"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
user_list = []
while True:
    user_list.append(input("Введи элемент списка"))
    a = input("Вводим следующий элемент?").lower()
    if a == "n":
        break
print(user_list)
y = 0
while y < len(user_list)-1:
    user_list[y],user_list[y+1] = user_list[y+1],user_list[y]
    y += 2
print(user_list)

#fast decision from teacher
user_answer = input("Введите список через запятую")
user_list = user_answer.split(",")
idx = 0
while idx < len(user_list) - 1:
    user_list[idx], user_list[idx+1] = user_list[idx+1], user_list[idx]
    idx += 2
print(user_list)