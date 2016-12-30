# -*- coding: utf-8 -*-
"""
Created on Sun May 29 18:34:46 2016

@author: John
"""

def alphascore(name):
	score = 0
	for letter in name:
		score += ord(letter)-64
	return score 	
#print(alphascore("COLIN"))


with open('names.txt') as f:
	lines = f.read().split(",")
	lines = sorted(lines)
	names = [str(name)[1:-1] for name in lines]
	scores = [alphascore(names[i])*(i+1) for i in range(len(names))]
print sum(scores)
		
