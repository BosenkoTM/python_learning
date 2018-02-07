#!/usr/bin/python
# -*- coding: utf-8 -*-

# Написать функцию, принимающую длину стороны квадрата и рассчитывающую периметр квадрата, его площадь и диагональ.
# Сделать два и более варианта функции, которые должна отличаться количеством возвращаемых переменных.
# Не забыть про проверки входных данных в самой функции.

x = 2


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def quadInfo(x: "длина стороны квадрата") -> "кортеж из периметра, площади и диагонали квадрата":
    if not isfloat(x):
        print("Вы ввели не число")
        return 0, 0, 0

    return x * 4, x * x, ((x ** 2) * 2) ** 0.6


print(quadInfo(x))

perimeter = 0
area = 0
diagonal = 0


def quadInfo2(x: "длина стороны квадрата"):
    if not isfloat(x):
        print("Вы ввели не число")
        return
    global perimeter, area, diagonal
    perimeter = x * 4
    area = x * x
    diagonal = ((x ** 2) * 2) ** 0.6


quadInfo2(x)
print(perimeter, area, diagonal)


def quadInfo3(x: "длина стороны квадрата") -> "список из периметра, площади и диагонали квадрата":
    if not isfloat(x):
        print("Вы ввели не число")
        return [0, 0, 0]

    return [x * 4, x * x, ((x ** 2) * 2) ** 0.6]


print(quadInfo3(x))


def quadInfo4(x: "длина стороны квадрата") -> "словарь из периметра, площади и диагонали квадрата":
    if not isfloat(x):
        print("Вы ввели не число")
        return {"периметр": 0, "площадь": 0, "диагональ квадрата": 0}

    return {"периметр": x * 4, "площадь": x * x, "диагональ квадрата": ((x ** 2) * 2) ** 0.6}


print(quadInfo4(x))
