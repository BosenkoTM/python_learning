#!/usr/bin/python
# -*- coding: utf-8 -*-

# Программа должна подсчитать количество строк, слов и букв в переданном ей файле.
# Имя файла должно передаваться в качестве первого аргумента после имени самого скрипта. Например, вызов скрипта в Linux через командную оболочку выглядит примерно так:
# python3 words.py text.txt

import sys

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

print("Количество строк %d" % len(lines))

words_count = 0
letter_count = 0
for line in lines:
    words = line.split()
    words_count += len(words)
    for letter in line:
        if letter.isalpha():
            letter_count += 1

print("Количество слов %d" % words_count)
print("Количество букв %d" % letter_count)
