#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3. Программа, которая считывает длины катетов прямоугольного треугольника и вычисляет длину его гипотенузы

number1 = int(raw_input('Введите длину первого катета: '))
number2 = int(raw_input('Введите длину второго катета: '))

hypotenuse = (number1 ** 2 + number2 ** 2) ** 0.5

print('Длина гипотенузы: {}'.format(hypotenuse))
