#!/usr/bin/python
# -*- coding: utf-8 -*-

# Вывести на экран числа от 1 до 5. Результат:
# 1 2 3 4 5

res = ""
for i in range(1, 6):
    res += str(i) + ' '
print(res)

res = ""
for i in '1', '2', '3', '4', '5':
    res += i + ' '
print(res)
