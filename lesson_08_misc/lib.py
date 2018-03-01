import random

# генерации двумерного массива случайных чисел с заданными размерами
def create_array(l: int, m: int) -> list:
    array = []
    for i in range(l):
        list_r = [random.randrange(1, 101, 1) for _ in range(m)]
        array.append(list_r)

    return array

# поиска максимальныъ чисел в каждой строке двумерного массива
def find_max_in_rows(array: list) -> list:
    """

    :param array:
    :return:
    :rtype: list
    """
    result = []
    for row in array:
        result.append(max(row))

    return result

# проверки любой переменной на то, что она содержит положительное целое число и приведение переменной к int
def to_int(i) -> [int, bool]:
    try:
        i = int(i)
        bool = True
    except ValueError:
        bool = False

    return i, bool