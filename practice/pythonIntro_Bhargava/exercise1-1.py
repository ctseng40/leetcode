#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 23:09:24 2020

@author: howard
"""


def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low+high)//2 #for python 3: // means floor division, e.g., 15//2=7
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
