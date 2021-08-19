"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
# 1 вариант
user_num = int(input("Введи число: "))
tem = 0
while user_num>0 and tem !=9:
    temp = user_num%10
    if temp>tem:
        tem = temp
    user_num //=10
print(f"Большая цифра в числе {tem}")

# 2 вариант
while True:
    ask_n = input("Введите целое положительное число:")
    if ask_n.isdigit():
        n_user = int(ask_n)
        break
    print("Вы ввели не число. Повторите ввод.")
temp = n_user
tmp = temp % 10
temp = temp // 10
while temp > 0:
    if temp % 10 > tmp:
        tmp = temp % 10
    temp = temp//10
print("Самая большая цифра из вашего числа", tmp)