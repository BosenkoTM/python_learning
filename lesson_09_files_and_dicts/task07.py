#!/usr/bin/python
# -*- coding: utf-8 -*-

# Сделать задачу 3 по словарям с текстом из файла `song.txt`

import sys
from . import task03

file_name = ''
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print("Укажите имя файла первым аргументом")
        exit()

print("Открываем файл %s" % file_name)
f = open(file_name, 'r', 1, "utf-8")
lines = f.readlines()
f.close()

string = ' '.join(lines)

task03.task03(string)
