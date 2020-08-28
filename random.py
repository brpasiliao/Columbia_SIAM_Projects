#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:36:20 2017

@author: Bian
"""

import random
"""
if random.random()<0.5:
    print("heads")
else:
    print("tails")
"""
flips = []
#heads = 0
#tails = 0

for i in range(1000):
    flip = ""
    if random.random()<0.5:
        flip = "heads"
#        heads += 1
    else:
        flip = "tails"
#        tails += 1
    flips.append(flip)

# print(flips)
# print("number of heads is " + str(heads))
# print("number of tails is " + str(tails))
heads = flips.count("heads")
tails = flips.count("tails")
print("number of heads is " + str(heads))
print("number of tails is " + str(tails))

probabilityOfHeads = heads / 1000
probabilityOfTails = tails / 1000

print("probability of heads is " + str(probabilityOfHeads))
print("probability of tails is " + str(probabilityOfTails))