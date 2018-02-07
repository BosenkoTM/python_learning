#!/usr/bin/python
# -*- coding: utf-8 -*-

# Написать функцию расчета аннуитетного платежа. Написать функцию расчета ежимесячного платежа.
# Рассчитать размер платежа при ипотеке 15 млн на 25 лет под 14% годовых.
# Мат. часть: http://biznes-kredit.info/malyj/raschet-annuitetnyh-platezhej-formula-excel.html

cabalaTime = 5  # срок ипотеки в годах
percent = 14  # годовая ставка
amount = 1500000  # сумма полученного кредита


# коэффициент аннуитета
def annuitetRatio(yearPercent: "годовая ставка", years: "срок ипотеки в годах"):
    monthPercent = yearPercent / 12
    monthRatio = monthPercent / 100
    months = years * 12
    x = (monthRatio + 1) ** months
    return monthRatio * x / (x - 1)


# размер платежа
def monthAmount(amount: "Размер кредита", yearPercent: "годовая ставка", years: "срок ипотеки в годах"):
    annuitet = annuitetRatio(yearPercent, years)
    print(annuitet)
    return amount * annuitet


print(monthAmount(amount, percent, cabalaTime))
