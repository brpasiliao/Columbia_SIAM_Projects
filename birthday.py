#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:56:36 2017

@author: Bian
"""

import datetime
# from datetime import date

print("Enter your birthday")
month = int(input("Month?(number) "))
day = int(input("Day? "))
year = int(input("Year? "))

birthday = datetime.date(year, month, day)
age = datetime.date.today() - birthday
print("You lived " + str(age))

if age.days > 5000:
    print("You're an old fart")
else:
    print("You're a baby")