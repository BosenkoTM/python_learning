#!/usr/bin/python
# -*- coding: utf-8 -*-

# Разработать три класса, которые следует связать между собой, используя наследование:
# 1. класс _Product_, который имеет три элемент-данных — имя, цена и вес товара (базовый класс для всех классов);
# 2. класс _Buy_, содержащий данные о количестве покупаемого товара в штуках, о цене за весь купленный товар и  о весе товара (производный класс для класса _Product_ и базовый класс для класса _Check_);
# 3. класс _Check_, не содержащий никаких элемент-данных. Данный класс должен выводить на экран информацию о товаре и о покупке ( производный класс для класса _Buy_);
# Программа должна содержать массив, заполненный объектами производных классов. В программе должно демонстрироваться использование всех разработанных элементов классов.


class Product:
    name = ""
    price = 0.0
    weight = 0.0
    def __init__(self, n):
        self.name = n

class Buy(Product):
    quantity = 0
    amount = 0.0
    def __init__(self, n, quantity):
        super(Buy, self).__init__(n)
        self.quantity = quantity
        self.amount = quantity * self.price

class Check(Buy):
    def __str__(self):
        return "Название {} цена {} вес {} количество{} сумма {}".format(self.name, self.price, self.weight, self.quantity, self.weight)


list = [Buy("Товар 1", 10), Check("Товар 2", 1), Check("Товар 3", 2)]

for r in list:
    print(r)
    print(r.__dict__)