#!/usr/bin/python
# -*- coding: utf-8 -*-

# Заполнить список из шести элементов произвольными целочисленными значениями. Вывести список на экран.

import random

listCount = 6  # Размер списка

# Вариант 1
randoms = [random.randrange(1, 101, 1) for _ in range(listCount)]
print(randoms)

# Вариант 2
randoms = []
for i in range(listCount):
    randoms.append(random.randrange(1, 101, 1))

# Вариант 3
randoms = []
for i in range(listCount):
    randoms.append(random.randint(1, 100))

print(randoms)
