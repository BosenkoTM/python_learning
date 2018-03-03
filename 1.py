#!/usr/bin/python
# -*- coding: utf-8 -*-

# Дано натуральное число n. Выведите все числа от 1 до n. Без использования циклов.

def get_decr(i: int):
    print("%d"%i)
    i -= 1
    if i > 0:
        get_decr(i)

get_decr(821)

