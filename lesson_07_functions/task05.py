#!/usr/bin/python
# -*- coding: utf-8 -*-

# Написать функцию, приминмающую номер месяца и возвращающую время года, которому принадледжит месяц.
# Не забыть про проверки входных данных в самой функции.
# Вызвать функцию в цикле несколько раз для случайных значений номера месяца.

import random


def season(m: "номер месяца от 1 до 12") -> "время года":
    mInt = int(m)
    season = "зима"
    if 2 < mInt < 6:
        season = "весна"
    elif 5 < mInt < 9:
        season = "лето"
    elif 8 < mInt < 12:
        season = "осень"
    elif 0 < mInt < 3 or mInt == 12:
        season = "зима"
    else:
        season = "ерунда"

    return season


randoms = [random.randrange(1, 12, 1) for _ in range(12)]

for i in randoms:
    print(i, season(i))
