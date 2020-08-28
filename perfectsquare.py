#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:24:14 2017

@author: Bian
"""

def is_square(number):
    if (number**(1/2)).is_integer():
        print("Your number is a perfect square")
        is_square(int(input("number: ")))
    else:
        print("Your number is not a perfect square")
        is_square(int(input("number: ")))
        
is_square(int(input("number: ")))