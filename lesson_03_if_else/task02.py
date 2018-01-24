#!/usr/bin/python
# -*- coding: utf-8 -*-

# 2. Определить четверть координатной плоскости по координатам x и y. Применить минимум два разных подхода в указании условий.


x = float(input('Введите координату x: '))
y = float(input('Введите координату y: '))

# Первый подход
q = 'центр координат'
if x > 0:
    if y > 0:
        q = 'I'
    elif y < 0:
        q = 'IV'
    else:
        q = 'ось Y'
elif x < 0:
    if y > 0:
        q = 'II'
    elif y < 0:
        q = 'III'
    else:
        q = 'ось Y'
elif y != 0:
    q = 'ось Y'

print('Четверть: ', q)

# Второй подход

if x > 0 and y > 0:
    q = 'I'
elif x < 0 < y:
    q = 'II'
elif x < 0 > y:
    q = 'III'
elif x > 0 > y:
    q = 'IV'
elif y != 0:
    q = 'ось Y'
elif x != 0:
    q = 'ось X'
else:
    q = 'центр координат'

print('Четверть: ', q)
