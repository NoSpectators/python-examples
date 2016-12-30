# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:52:00 2016

@author: John
"""

def Consecutive(arr): 

    # get min and max values of array
    mi = min(arr)
    ma = max(arr)
      
    # numbers needed to fill array are all numbers in
    # between max and min minus the other elements in the array
    #print ma, mi, len(arr)-1
    return ma - mi - (len(arr) - 1)
    
# keep this function call here  
print Consecutive([5,10,15])