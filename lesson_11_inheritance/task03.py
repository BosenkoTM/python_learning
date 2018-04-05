#!/usr/bin/python
# -*- coding: utf-8 -*-

# **Phone**: id, Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки,
# Дебет, Кредит, Время городских и междугородных разговоров.
# Создать массив объектов. Вывести:
# a) сведения об абонентах, у которых время внутригородских разговоров превышает заданное;
# b) сведения об абонентах, которые пользовались междугородной связью;
# c) сведения об абонентах в алфавитном порядке.
# Создать классы, спецификации которых приведены ниже. Определить конструкторы . Определить дополнительно методы `__str__`.
# Определить дополнительно методы в классе, создающие массив объектов. Задать критерий выбора данных и вывести эти данные на консоль.

import random

class Phone:
    id = 0  # id
    fname = ""  # Фамилия
    lname = ""  # Имя
    tname = ""  # Отчество
    address = ""  # Адрес
    credit_card = 0  # Номер кредитной карточки
    debit = 0.0 # Дебет
    credit = 0.0  # Кредит
    local_calls_time = 0  # Время городских разговоров
    out_calls_time = 0  # Время междугородных разговоров

    def __str__(self):
        return 'Абонент ID: {} ФИО: {} Адрес: {}'.format(self.id, self.fname, self.lname, self.tname, self.address)

    def fill_rand(self):
        self.id = random.randrange(1, 1001, 1)
        self.fname ="fname {}".format(self.id)
        self.lname ="lname {}".format(self.id)
        self.address ="address {}".format(self.id)
        self.address ="address {}".format(self.id)
        self.local_calls_time = random.randrange(1, 101, 1)
        self.out_calls_time = random.randrange(1, 10, 1)
        return self

    @staticmethod
    def create_list(size):
        arr = []
        for x in range(0, size):
            arr.append(Phone().fill_rand())
        return arr


phones = Phone.create_list(10)

print("сведения об абонентах, у которых время внутригородских разговоров превышает заданное")
for onePhone in phones:
    if onePhone.local_calls_time > 10:
        print(onePhone)

print("сведения об абонентах, которые пользовались междугородной связью")
for onePhone in phones:
    if onePhone.out_calls_time > 0:
        print(onePhone)

print("сведения об абонентах в алфавитном порядке")
list_for_sort = [(onePhone.fname, onePhone) for onePhone in phones]

list_for_sort.sort()

for onePhone in list_for_sort:
    print(onePhone[1])