#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
 s_1 = input("Enter the first line: ")
 s_2 = input("Enter the second line: ")

 set1 = set(s_1)
 set2 = set(s_2)

 common_characters = set1.intersection(set2)

 print("Common characters:", common_characters)
