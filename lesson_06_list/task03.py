#!/usr/bin/python
# -*- coding: utf-8 -*-

# Заполнить список из шести элементов произвольными целочисленными значениями. Вывести список на экран в обратной последовательности.
# Два варианта получения обратной последовательности: с приминением цикла и без него.

import random

listCount = 6  # Размер списка

randoms = [random.randrange(1, 101, 1) for _ in range(listCount)]
print('Исходный список ', randoms)
# Вариант 1
randoms.reverse()
print(randoms)

# Вариант 1
reversedList = []
listLength = len(randoms)
for i in range(listLength):
    reversedList.append(randoms[i])
    randoms.reverse()
print(randoms)
