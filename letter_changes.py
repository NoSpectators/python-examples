# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 22:12:19 2016

@author: John
"""

def LetterChanges(string): 

    # code goes here 
    vowels = ['a','e','i','o','u']
    str1 = ""
    for i in range(len(string)):
        if string[i].isalpha():
            str1 += chr(ord(string[i])+1)
        else:
            str1 += chr(ord(string[i]))    
    str2 = ""
    for i in str1:
        if i not in vowels:
            str2 += i
        else:
            str2 += i.upper()            
        
    return str2
    
# keep this function call here  
print LetterChanges("fun times!")
  
