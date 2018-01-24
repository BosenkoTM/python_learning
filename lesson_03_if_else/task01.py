#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1. Вычислить модуль числа без использования библиотечных функций.


number = int(input('Введите число: '))

mod = number
if mod < 0: mod *= -1

print('Модуль числа {} = {}'.format(number, mod))
