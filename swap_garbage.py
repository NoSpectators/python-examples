# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:34:19 2016

@author: John
"""

def swap(string):
    
    new = bytearray(string)
    new[0], new[len(string)-1] = new[len(string)-1],new[0]
        
    return str(new)
            
print swap("ahello6llz")
            
























"""
temp = x
x = y
y = x"""