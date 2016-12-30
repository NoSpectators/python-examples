# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:02:13 2016

@author: John
"""

def WordSplit(strArr): 

    word = strArr[0]
    s = set(strArr[1].split(','))
    #print s
    for i in range(len(word)):
        a = strArr[0][:i]
        #print a

        b = strArr[0][i:]
        #print b
        if a in s and b in s:
            #print a, b
            return a + ',' + b
    return 'not possible'
    
# keep this function call here  
print WordSplit(["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"])