"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в
формате чч:мм:сс. Используйте форматирование строк.
"""
while True:
    user_time = input("Введи время в секундах\n")
    if user_time.isdigit():
        user_time = int(user_time)
        break
    print("Введи не число")

hour,minute, sec = user_time // 3600, (user_time//3600) % 60, user_time % 60
print(f"{hour:>02}:{minute:>02}:{sec:>02}")