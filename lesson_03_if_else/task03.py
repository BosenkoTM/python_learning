#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3. Проверить, что хотя бы одно из чисел a или b оканчивается на 0.


a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

if not(a % 10) or not(b % 10):
    print('оканчивается')
else:
    print('НЕ оканчивается')
