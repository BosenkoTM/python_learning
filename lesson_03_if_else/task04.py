#!/usr/bin/python
# -*- coding: utf-8 -*-

# 4. Дана следующая функция y = f(x):
# y = x + 1.5, при x > 10;
# y = 0, при x = 10;
# y = -x, при x < 10.


x = float(input('Введите число x: '))

y = 0
if x > 10:
    y = x + 1.5
elif x < 10:
    y = -x

print('y={}'.format(y))
