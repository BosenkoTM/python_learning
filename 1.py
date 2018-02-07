#!/usr/bin/python
# -*- coding: utf-8 -*-

lst = [1, 3, 6, 9, 11, 11, 10, 8]

for i in lst:
    if i % 3 != 0:
        print(i)
        print(lst)
        lst.remove(i)
        print(lst)

print(lst)