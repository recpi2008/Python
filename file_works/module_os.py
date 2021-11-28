import os

"""
Предоставляет широкий спектр функций для работы с файлами
remove() - удаляет файл из директории
rename() - переименовывает файл
listdir() - файлы в указанной директории

os.path.basename()- возвращает название файла пути
os.path.dirname() - возвращает часть каталога пути
os.path.exists() - проверяет, присутствует ли указанный файл
os.path.isdir(), os.path.isfile() - проверяет, является ли объект папкой или файлом
os.path.join() - позволяет объединить несколько путей
os.path.split() - разделяет путь на кортеж, содержащий и путь до каталога, и имя файла.

"""
os.rename("text", "my_text")

content = os.listdir(path=".")
print(content)

print(os.path.basename("/Users/u18544521/PycharmProjects/GeekBrains/lesson5/text"))
print(os.path.dirname("/Users/u18544521/PycharmProjects/GeekBrains/lesson5/text"))
print(os.path.exists("/Users/u18544521/PycharmProjects/GeekBrains/lesson5/text"))
print(os.path.exists("/Users/u18544521/PycharmProjects/GeekBrains/lesson5/my_text"))
print(os.path.isfile("/Users/u18544521/PycharmProjects/GeekBrains/lesson5/my_text"))
print(os.path.isdir("/Users/u18544521/PycharmProjects/GeekBrains/lesson5/my_text"))
print(os.path.isdir("/Users/u18544521/PycharmProjects/GeekBrains/lesson5"))
print(os.path.join("/Users/u18544521/PycharmProjects/", "GeekBrains/lesson5/text"))
print(os.path.split("/Users/u18544521/PycharmProjects/GeekBrains/lesson5/text"))

os.remove("my_text")





