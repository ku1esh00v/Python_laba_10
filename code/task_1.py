#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    glassnie = {'a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у',
                'ы', 'э', 'ю', 'я'}

    s = input("Введите строку: ")

    counter = len([i for i in s.lower() if i in glassnie])

    print("Количество гласных в строке:", counter)
