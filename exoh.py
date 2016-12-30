# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:38:05 2016

@author: John
"""

def ExOh(string): 

    # code goes here 
    if len(string) < 2:
        return "false"
    dict1 = {}
    for i in string:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    
    counts = [dict1[key] for key in dict1]
    for i in range(len(counts)-1):
        if counts[i] == counts[i+1]:
            return "true"
        return "false"
# keep this function call here  
print ExOh("xoxo")#true
print ExOh("x")#false
print ExOh("xxoo")  #true
print ExOh("xxooo")