#!/usr/bin/python
# -*- coding: utf-8 -*-

# Написать функцию, возвращающую два введеных с клавиатуры числа.

def inputTwoNumbers():
    m = int(input('Введите первое число: '))
    n = int(input('Введите второе число: '))
    return m, n


print(inputTwoNumbers())
