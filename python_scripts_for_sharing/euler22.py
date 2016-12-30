# -*- coding: utf-8 -*-
"""
Created on Sun May 29 18:34:46 2016

@author: John
"""

def alphabetical_worth(name):
	dict = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8,
			"i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15,
			"p":16, "q":17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 
			'w':23, 'x':24, 'y':25, 'z':26}
	name = name.lower()
	name_score = 0
	for letter in name:
		for key in dict:
			if letter == key:
				name_score += dict[key]
	return name_score 	
	
	
total_scores = []
with open('names.txt') as f:
	lines = f.read().split(",")
	lines = sorted(lines)
	for i in range(len(lines)):
		name = str(lines[i][1:-1])
		total_scores.append(alphabetical_worth(name)* (i+1)) 
		
print total_scores[937]
print sum(total_scores)
		

#test--COLIN is name 938. This name should have a score of 53
#for i in range(len(lines)):
	#name = str(lines[i][1:-1])
	#print name, i 
	#letter_score = 0
	#if name == 'COLIN':
	#print name, i