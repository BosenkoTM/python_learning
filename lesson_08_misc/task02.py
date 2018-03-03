#!/usr/bin/python
# -*- coding: utf-8 -*-

# Дано натуральное число n. Выведите все числа от 1 до n. Без использования циклов.


def get_decr(i: int) -> int:
    print("%d\n", i)
    i -= 1
    if i > 1:
        get_decr(i)

get_decr(821)

