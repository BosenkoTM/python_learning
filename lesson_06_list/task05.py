#!/usr/bin/python
# -*- coding: utf-8 -*-

# Заполнить список из десяти элементов произвольными целочисленными значениями. Получить список из элементов певрого списка,
# стоящих на четных местах.

import random

listCount = 10  # Размер списка

randoms = [random.randrange(1, 101, 1) for _ in range(listCount)]
print('Исходный список ', randoms)

# Вариант 1
res = []
for i in range(len(randoms)) :
    if i % 2 == 0:
        res.append(randoms[i])

print(res)

# Вариант 2
res = []
foo = 0
for i in randoms :
    if foo == 0 :
        res.append(i)
        foo = -2
    foo += 1

print(res)
