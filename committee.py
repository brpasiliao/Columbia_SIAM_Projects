#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:57:57 2017

@author: Bian
"""
import random

# men = 60
# women = 40
# committee = men + women

chances = 0

for h in range(10000):
    men = 0
    women = 0
    
    for i in range(10):
        person = random.random()
        
        if person < .6:
            men += 1
        else:
            women += 1
    
                
    if men == women: 
        chances += 1
    

probability = chances / 10000
print(probability)
    