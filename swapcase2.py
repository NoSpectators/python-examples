# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:34:19 2016

@author: John
"""

def SwapII(string):
    output = bytearray()
    lastNum = None
    #swap cases
    for i in range(len(string)):
        char = string[i]
        output += char.swapcase()
        #swap numbers 
        if char.isdigit():
            if not lastNum is None:
                output[i], output[lastNum] = output[lastNum], output[i]
            lastNum = i
        elif not char.isalpha():
            lastNum = None
    return str(output)
            
print SwapII("5hello6ll5")
            
























"""
temp = x
x = y
y = x"""