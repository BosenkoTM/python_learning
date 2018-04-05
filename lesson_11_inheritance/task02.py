#!/usr/bin/python
# -*- coding: utf-8 -*-

# Написать класс калькулятора, хранящего вещественное число x и понимающего следующие команды:
# * прибавить к этому числу значение параметра,
# * вычесть из него,
# * домножить его и разделить,
# * а также извлечь из этого числа квадратный корень
# * и взять тригонометрическую функцию.
# Написать еще один класс, кроме перечисленного имеющий одно свойство и понимающий команды _записать в память_, _извлечь из памяти_, _добавить x к содержимому памяти_.

import math
class Calc:
    x = 0.0
    def __init__(self, x):
        self.x = x
    def plus(self, p):
        self.x += p
        return self
    def minus(self, p):
        self.x -= p
        return self
    def mul(self, p):
        self.x *= p
        return self
    def dev(self, p):
        self.x /= p
        return self
    def sqrt(self):
        self.x = self.x ** 0.5
        return self
    def cos(self):
        return math.cos(self.x)

class SuperCalc(Calc):
    y = 0.0
    def set(self, y):
        self.y = y
        return self
    def get(self):
        return self.y
    def sum_x(self):
        self.y += self.x
        return self

c = SuperCalc(0)
y = c.dev(1).mul(2).plus(10.1).set(1).sum_x().get()