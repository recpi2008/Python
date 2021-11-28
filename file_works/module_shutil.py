import shutil

"""
Для выполнения операций с файлами и папками: 
копирование, перемещение, удаление.

copy() - копирования содержимого или текста исходного файла в конечный файл
copyfile() - копирование файла
copyfileobj() - Копирование содержимого одного файлового объекта (f_obj_1) в другой (f_obj_2)
move(file, path) - Перемещение файла или директории в указанную директорию
rmtree(path) - удаление директории
"""

shutil.copy("my_text", "my_text_copy")
shutil.copyfile("my_text", "my_text_copy_2")

with open("my_text_copy_2", "w") as fw:
    print("\nЕще ты дремлешь, друг прелестный", file=fw)

shutil.move("my_text", "/Users/u18544521/PycharmProjects/GeekBrains/lesson4")


shutil.move("/Users/u18544521/PycharmProjects/GeekBrains/lesson4/text", "text_copy")
shutil.rmtree("/Users/u18544521/PycharmProjects/GeekBrains/lesson5")