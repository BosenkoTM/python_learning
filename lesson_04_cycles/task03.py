#!/usr/bin/python
# -*- coding: utf-8 -*-

# Пользователь вводит любое целое положительное число (сделать проверку).
# Программа должна просуммировать все числа от 1 до введенного пользователем числа (не включая его).

x = input('Введите целое положительное число: ')

if not x.isdigit():
    print("Вы ввели не число")
    exit()

xInt = int(x)
if xInt < 1:
    print("Число не положительное")
    exit()

sumNumbers = 0
for i in range(1, xInt):
    sumNumbers += i

print("Сумма", sumNumbers)


sumNumbers = 0
i = 1
while i < xInt:
    sumNumbers += i
    i += 1

print("Сумма", sumNumbers)