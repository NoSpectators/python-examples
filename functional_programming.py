# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 14:21:36 2016

@author: John
"""
a = range(1,20)
b = []
def double(x):
    return x * 2
    
for i in a:
    b.append(double(i))

print b

#easier
b = [x*2 for x in a]
print b

print map(double,a)
def is_even(x):
    return x % 2 == 0
print is_even(2)
print is_even(3)

#alternate
print filter(is_even,(a))

def sum(x,y):
    return x+y
print sum(1,2)

#alternate
print reduce(sum,a) #sums the list a 

c = []
#but you can't use reduce with empty list unless..
print reduce(sum,c,0)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print factorial(5)

def mult3(n):
    if n == 1:
        return 3
    else:
        return mult3(n-1) + 3

for i in range(1,10):
    print(mult3(i))