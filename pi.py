#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 16:10:42 2017

@author: Bian
"""

import random



points =[]

for point in range(1000):
    
    distance = (random.random()**2 + random.random()**2) ** 0.5
    if distance < 1:
        points.append("true")
    else:
        points.append("false")

lessThan1 = points.count("true")
moreThan1 = points.count("false")

probabilityLess = lessThan1 / 1000
probabilityMore = moreThan1 / 1000

print("The probability that the point is less than 1 unit of distance away from the origin is " + str(probabilityLess))
print("The probability that the point is more than 1 unit of distance away from the origin is " + str(probabilityMore))
