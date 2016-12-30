# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 17:08:08 2016

@author: John
"""


	
def PrimeMover(num): 
   primes = []
   n = 2
   while len(primes) != num:#gets primes up to number
   
      pr = True  #initialize a flag 
      for i in range(0, len(primes)):
         if n % primes[i] == 0:
            #print "n % primes[i] = ", 9 % primes[i], primes[i]
            n += 1
            pr = False
            break
      if pr:
      	primes.append(n)
   #print primes
   return primes[-1]
        
        
        

print PrimeMover(9)  
