#!/usr/bin/python
# -*- coding: utf-8 -*-

# Заполнить список из десяти элементов произвольными целочисленными значениями.
# Затем четные элементы расположить в начале списка, нечетные - в конце.

import random

listCount = 10  # Размер списка

randoms = [random.randint(1, 101) for _ in range(listCount)]
print('Исходный список ', randoms)

even = [] # Четные
odd = [] # Нечетные

for i in range(len(randoms)) :
    if i % 2 == 0 :
        even.append(randoms[i])
    else :
        odd.append(randoms[i])

print('Четные: ', even)
print('Нечетные: ', odd)

res = [i for i in even]
res.extend([i for i in odd])

print('Общий список: ', res)