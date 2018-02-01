#!/usr/bin/python
# -*- coding: utf-8 -*-

# Посчитать количество слов в введёном с клавиатуры предложении.

sentence = input('Введите предложение из нескольких слов: ')

# Убираем повторяющиеся пробелы
while sentence != sentence.replace('  ', ' '):
    sentence = sentence.replace('  ', ' ')

wordCount = len(sentence.split(' '))
print('Количество слов: %d' % wordCount)