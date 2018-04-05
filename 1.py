#!/usr/bin/python
# -*- coding: utf-8 -*-

# Создайте класс с именем _Person_, содержащий три поля для хранения имени, фамилии и отчества.
# В классе создайте функцию _show_data()_, выводящую на экран имя, фамилию и отчество.
# Далее от класса _Person_ с помощью наследования создайте два класса: _Student_, _Professor_.
# К классу _Student_ добавьте дополнительное поле, содержащее средний бал студента.
# К классу _Professor_ три поля:
# 1. число публикаций профессора,
# 2. должность (тип - перечисление) - преподаватель, старший преподаватель, доцент, профессор,
# 3. возраст.
# Для каждого производного класса переопределите метод _show_data()_.
# В основной программе определите массив.
# Далее в цикле нужно организовать ввод студентов и профессоров вперемешку.
# Когда ввод будет закончен, нужно вывести информацию с помощью метода _show_data()_ обо всех людях.

import math
class Calc:
    x = 0.0
    def __init__(self, x):
        self.x = x
    def plus(self, p):
        self.x += p
    def minus(self, p):
        self.x -= p
    def mul(self, p):
        self.x *= p
    def dev(self, p):
        self.x /= p
    def sqrt(self):
        self.x = self.x ** 0.5
    def cos(self):
        return math.cos(self.x)

class SuperCalc(Calc):
    y = 0.0
    def set(self, y):
        self.y = y
    def get(self):
        return self.y
    def sum_x(self):
        self.y += self.x
