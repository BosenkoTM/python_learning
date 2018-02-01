#!/usr/bin/python
# -*- coding: utf-8 -*-

# Заполнить список из четырёх элементов введёными строковыми значениями. Вывести список на экран.

listStr = []
for i in range(1, 5):
    string = input('Введите любую строку: ')
    listStr.append(string)

print(listStr)
