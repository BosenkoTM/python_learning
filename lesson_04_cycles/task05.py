#!/usr/bin/python
# -*- coding: utf-8 -*-

# Найдите количество четных цифр введёного натурального числа.

x = input('Введите натуральное число: ')

if not x.isdigit():
    print("Вы ввели не число")
    exit()

xInt = int(x)
if xInt < 1:
    print("Число не натуральное")
    exit()

count = 0
while xInt != 0:
    if xInt % 2 == 0:
        count += 1
    xInt //= 10

print(count)
