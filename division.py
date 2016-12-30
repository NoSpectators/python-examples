# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 19:41:32 2016

@author: John
"""
#greatest common divisor
def  Division(n1, n2):
    
    if n1 % n2 == 0:
        return min(n1,n2)
    if n2 % n1 == 0:
        return min(n1,n2)
    f1=[i for i in range(1,n1) if n1 % i == 0]
    f2=[j for j in range(1,n2) if n2 % j == 0]
    
    both = [i for i in f1 if i in f2]
        
    return max(both)    

print Division(14,28)
print Division(8,2)