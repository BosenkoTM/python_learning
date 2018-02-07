#!/usr/bin/python
# -*- coding: utf-8 -*-

# Работаем с чужим кодом. В коде из файла https://github.com/groall/python_learning/blob/master/lesson_04_cycles/task03.py нужно
# заменить повторяющееся с циклах действие суммирования на вызов функции, функция должна работать с глобальной переменной `sumNumbers`.

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


def sumToNumbers(i):
    global sumNumbers
    sumNumbers += i


for i in range(1, xInt):
    sumToNumbers(i)

print("Сумма", sumNumbers)

sumNumbers = 0
i = 1
while i < xInt:
    sumToNumbers(i)
    i += 1

print("Сумма", sumNumbers)
