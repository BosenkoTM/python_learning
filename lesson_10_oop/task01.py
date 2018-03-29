#!/usr/bin/python
# -*- coding: utf-8 -*-

# Создать класс Circle, конструктор которого принимает радиус. Класс должен иметь два метода, вычисляющие площадь и длину окружности.

import math

class Circle:
    r = 0
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r
    def perimeter(self):
        return 2 *math.pi * self.r

NewCircle = Circle(8)
print(NewCircle.area()) #201.06192982974676
print(NewCircle.perimeter()) #50.26548245743669
