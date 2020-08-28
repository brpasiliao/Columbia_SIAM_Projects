#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:57:57 2017

@author: Bian
"""
import random
'''

# --------------------------------------------3-committee
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

# --------------------------------------------6-frog

times = 0
for h in range(10000):
    x = 0
    y = 0

    for i in range(20):
    
        if x == y:
            if random.random() < .5:
                x += 1
            else: 
                y += 1   
        elif x > y:
            if random.random() < 1/3:
                x += 1
            else:
                y += 1
                
        else:
            if random.random() < 1/3:
                y += 1
            else:
                x += 1
            
    if x == y:
        times += 1
        
probability = times / 10000
print(probability)

'''

# ----------------------------------------------9-pirates

win = False

trials = 0
dieroll = 0
chanceToLose = 5/6
chanceToWin = 1/6

alice = 0
bob = 0
charlie = 0
    
    
while win == False:
    chanceToWin = (chanceToLose ** dieroll) * chanceToWin
    dieroll += 1
    print(chanceToWin)
    
    if random.random() < chanceToWin:
        win = True
        if dieroll == 1:
            alice += 1
        elif dieroll == 2:
            bob += 1
        else:
            charlie += 1
            
    else: 
        if dieroll > 3:
            dieroll = 0
            chanceToLose = 5/6
            chanceToWin = 1/6       
    
    trials += 1



    
    
    
    
    
    
    
    
    
    
    
    
    