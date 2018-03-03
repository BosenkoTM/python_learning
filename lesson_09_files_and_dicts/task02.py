#!/usr/bin/python
# -*- coding: utf-8 -*-

# Дан список чисел, который может содержать до 100000 чисел (каждое число от 0 до 1000). Определите, сколько в нем встречается различных чисел.
# Эту задачу на Питоне можно решить в одну строчку, но нам нужно с помощью словаря.

import random

randoms = [random.randrange(1, 1000, 1) for _ in range(100000)]

uniq = {}
for i in randoms:
    if i not in uniq:
        uniq[i] = 1
    else:
        uniq[i] += 1

print(uniq)
