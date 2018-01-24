#!/usr/bin/python
# -*- coding: utf-8 -*-

# 5. Проверить, что введеные три числа (длины сторон) могут образовать треугольник.


a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

triangle = (a + b) > c and (a + c) > b and (c + b) > a

if triangle:
    print('Треугольник возможен')
else:
    print('Треугольник НЕвозможен')
