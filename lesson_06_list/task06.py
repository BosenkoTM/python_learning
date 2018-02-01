#!/usr/bin/python
# -*- coding: utf-8 -*-

# Заполнить список из шести элементов квадратными корнями произвольныз целочисленныз значений. Вывести список на экран через запятую.

import random
import math

listCount = 10  # Размер списка

randoms = [str(math.sqrt(random.randint(1, 101))) for _ in range(listCount)]
print('Исходный список ', randoms)

print(', '.join(randoms))
