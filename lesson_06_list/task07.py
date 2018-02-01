#!/usr/bin/python
# -*- coding: utf-8 -*-

# Заполнить список из десяти элементов произвольными целочисленными значениями (без использования цикла).
# Удалить те элементы, значения которых не кратны 3.

import random

listCount = 10  # Размер списка

randoms = [random.randint(1, 101) for _ in range(listCount)]
print('Исходный список ', randoms)

res = []

for i in randoms :
    if i % 3 == 0 :
        res.append(i)

print(res)