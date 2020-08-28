#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 13:33:05 2017

@author: Bian
"""

my_sum = []

print("enter 5 numbers")
my_sum.append(int(input("first number: ")))
my_sum.append(int(input("second number: ")))
my_sum.append(int(input("third number: ")))
my_sum.append(int(input("fourth number: ")))
my_sum.append(int(input("fifth number: ")))

print(my_sum)
sum = 0

for num in my_sum:
    sum = sum + num

print("Your total is " + str(sum))
