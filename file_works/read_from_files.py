"""
Работа с текстовыми файлами
префикс r - для экранирвоания символов и встроенных конструкций
open - открывает файл
read() - извлекает весь контент целиком
read(1024) - извлекает c ограничением в килобайт
readline() - извлекает построчно
readlines() - извлекает строки в список
write() - запись в файл
tell() - определяет, в скольких байтах от начала файла находится указатель
seek() - переход на нужную позицию


Режимы доступа к файлу
r - Открыть файл на чтение (режим по умолчанию)
w - Открыть на запись. При этом удалить содержимое файла. Если файла нет, создать новый.
x - Открыть файл на запись, если его нет. Если файл есть, он не будет создан.
a - Открыть файл на дозапись. Добавить информацию в конец файла.
b - Открыть файл в двоичном формате.
t - Открыть файл в текстовом формате (режим по умолчанию)
+ - Открыть файл на чтение и запись

Параметры файлового объекта
mode - возвращает режим доступа файлового объекта
closed - открыт файл или закрыт
name - имя файла
"""

file_obj = open("text", 'w')
file_obj.write("Мороз и солнце, день чудесный!")
file_obj.close()

file_obj = open("text")
print(file_obj.read(1))
print(file_obj.tell())
print(file_obj.read())
print(file_obj.seek(3, 0))
file_obj.close()

file_obj = open("text")
print(file_obj.readlines())
file_obj.close()

file_obj_w = open("text")
for line in file_obj_w:
    print(line)
    print(file_obj_w.closed)
file_obj_w.close()
print(file_obj_w.closed)

with open("text", 'a') as file_obj_w:
    print("\nЕще ты дремлешь, друг прелестный", file=file_obj_w)

file_obj = open("text")
print(file_obj.readline())
file_obj.close()


