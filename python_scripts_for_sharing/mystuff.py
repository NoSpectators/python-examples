# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:54:21 2016

@author: John
"""
#dictionary
mystuff = {'apple':'I AM APPLES!'}
print mystuff['apple']

#module way #import mystuff; mystuff.apple()
def apple():
    print 'I AM APPLES!'

#module way #import mystuff; mystuff.tangerine
tangerine = "living reflection of a dream"


#class way 
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between!"
    
    def apple(self):
        print 'I am classy apples!'

thing = MyStuff() #instantiates the class
thing.apple()
print thing.tangerine

    
    