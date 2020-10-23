#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:42:34 2020

@author: howard
"""

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total
print(sum([1,2,3,4]))