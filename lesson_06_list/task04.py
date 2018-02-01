#!/usr/bin/python
# -*- coding: utf-8 -*-

# Заполнить список из шести элементов произвольными целочисленными значениями.
# Найти максимальный элемент в списке, вывести его и его номер на экран.
# Два варианта вычисления максимального элемента: с приминением цикла и без него.

import random

listCount = 6  # Размер списка

randoms = [random.randrange(1, 101, 1) for _ in range(listCount)]
print('Исходный список ', randoms)

# Вариант 1
maxInt = 0
maxIntIndex = 0
for i in range(len(randoms)) :
    if randoms[i] >= maxInt :
        maxInt = randoms[i]
        maxIntIndex = i

print('Максимальное число %d и его индекс %d' % (maxInt, maxIntIndex))

# Вариант 2
maxInt = max(randoms)
maxIntIndex = randoms.index(maxInt)

print('Максимальное число %d и его индекс %d' % (maxInt, maxIntIndex))
