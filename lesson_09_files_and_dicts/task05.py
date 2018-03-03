#!/usr/bin/python
# -*- coding: utf-8 -*-

# Вводится имя файла. Требуется проверить, что его расширение входит в список допустимых (png, jpg, jpeg, gif, svg').

allow_ext = ['png', 'jpg', 'jpeg', 'gif', 'svg']

file_name = input("Введите имя файла: ")

file_name_list = file_name.split('.')

ext = ''
if len(file_name_list) > 1:
    ext = file_name_list[len(file_name_list) - 1]
    print("Расширение %s" % ext)
    if ext in allow_ext:
        print("Разрешено")
    else:
        print("Запрещено")
else:
    print("Введёное имя файла не имеет расширения")
