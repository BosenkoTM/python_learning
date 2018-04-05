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


class Person:
    name = ""
    fname = ""
    tname = ""
    def show_data(self):
        print("ФИО {} {} {}".format(self.name, self.fname, self.tname))

class Student(Person):
    grade = 0
    def show_data(self):
        print("ФИО {} {} {}, средний бал {}".format(self.name, self.fname, self.tname, self.grade))

class Professor(Person):
    pub_count = 0
    position = ""
    age = 0
    def show_data(self):
        print("ФИО {} {} {} число публикаций  {}, должность {}, возраст {}".format(self.name, self.fname, self.tname, self.pub_count, self.position, self.age))

list = [Student(), Student(), Professor(), Professor(), Student()]

for p in list:
    p.show_data()
