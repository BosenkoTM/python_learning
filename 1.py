#!/usr/bin/python
# -*- coding: utf-8 -*-

# Дан текст:
# Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille Buonaparte. Non, je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous permettez encore de pallier toutes les infamies, toutes les atrocités de cet Antichrist (ma parole, j'y crois) — je ne vous connais plus, vous n'êtes plus mon ami, vous n'êtes plus мой верный раб, comme vous dites
# Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их частоты появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.
# *Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
# Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости слова и само слово.
# Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу,
# а если они равны — то по второму. Это почти то, что требуется в задаче.*

str = "Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille Buonaparte. Non, je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous permettez encore de pallier toutes les infamies, toutes les atrocités de cet Antichrist (ma parole, j'y crois) — je ne vous connais plus, vous n'êtes plus mon ami, vous n'êtes plus мой верный раб, comme vous dites"

dic = {}
str_arr = str.split()
for word_number in range(len(str_arr)):
    word = str_arr[word_number]
    if word not in dic :
        dic[word] = 1
    else:
        dic[word] += 1

list_for_sort = [(item[1], item[0]) for item in dic.items()]

list_for_sort.sort()
list_for_sort.reverse()

dic_for_group = {}

for item in list_for_sort :
    word_count = item[0]
    word = item[1]
    if word_count not in dic_for_group :
        dic_for_group[word_count] = [word]
    else:
        dic_for_group[word_count].append(word)

for key, words in dic_for_group.items() :
    words.reverse()
    print(key)
    print(words)
