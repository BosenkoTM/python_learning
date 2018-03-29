#!/usr/bin/python
# -*- coding: utf-8 -*-

# Создать класс Rectangle, конструктор которого принимает длину и ширину. Класс должен иметь два метода, вычисляющие площадь и периметр прямоугольника.

import math

class Rectangle:
    h = 0
    w = 0
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)

NewRectangle = Rectangle(8, 4)
print(NewRectangle.area()) #32
print(NewRectangle.perimeter()) #24
