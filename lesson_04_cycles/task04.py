#!/usr/bin/python
# -*- coding: utf-8 -*-

# Найдите произведение цифр трехзначного числа, введёного с клавиатуре.

x = input('Введите целое положительное число: ')

if not x.isdigit():
    print("Вы ввели не число")
    exit()

xInt = int(x)
if xInt < 100 or xInt > 999:
    print("Число не трехзначное")
    exit()


print("Произведение цифр введёного числа ", comp)

comp = 1
while xInt != 0:
    comp *= xInt % 10
    xInt //= 10

print("Произведение цифр введёного числа ", comp)
