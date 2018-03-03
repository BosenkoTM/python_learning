#!/usr/bin/python
# -*- coding: utf-8 -*-

# С помощью словаря из файла `codes.txt` расшифровать текст `006005034028017006029034028017006006017036034028020021029034028017028017`

import sys

file_name = ''
if __name__ == "__main__":
    if len (sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print ("Укажите имя файла первым аргументом")
        exit()

print("Открываем файл %s"%file_name)
f = open(file_name, 'r', 1, "utf-8")
lines = f.readlines()
f.close()

codes = {}
for line in lines :
    codeList = line.split("\t")
    codes[codeList[1].strip()] = codeList[0]

encoded_string = "006005034028017006029034028017006006017036034028020021029034028017028017"
if len(encoded_string) % 3 != 0 :
        print ("Зашифрованная строка не содержит корректный шифр")
        exit()

decoded_string = ""
for i in range(0, (len(encoded_string) // 3) - 1) :
    encoded_letter = encoded_string[i*3: i*3 + 3]
    if encoded_letter in codes :
        decoded_letter = codes[encoded_letter]
        decoded_string += decoded_letter
    else :
        print("Шифр %s не найден"%encoded_letter)

print(decoded_string)
