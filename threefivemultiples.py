# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:39:44 2016

@author: John
"""

def ThreeFiveMultiples(num): 
    
    total = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            total += i
        
    # code goes here 
    return total
    
# keep this function call here  
print ThreeFiveMultiples(6)#8 
print ThreeFiveMultiples(1) 