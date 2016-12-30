# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 23:06:12 2016

@author: John
"""


def StringScramble(str1, str2):

    arr1 = list(str1)
    for x in str2:
      if x in arr1:
        arr1[arr1.index(x)] = ' '
        #print arr1
      else:
        return "false"
    return "true"
    
# keep this function call here  
print StringScramble("cdore","coder")
print StringScramble("h3llko", "hello")












  