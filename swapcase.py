# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:34:19 2016

@author: John
"""

def SwapCase(string):
    new_str=""
    for i in string:
        if i.isalpha():
            if i.islower():
                new_str += i.upper()
            elif i.isupper():
                new_str += i.lower()
        else:
            new_str += i
    
    return new_str
    
    
print SwapCase("Hello-LOL")