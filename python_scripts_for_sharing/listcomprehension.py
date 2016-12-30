def listComprehension():
	a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	even = [i for i in a if i%2 == 0]
	common = [i for i in b if i in c]
	print even
	print common 
	print 'without list comprehensions:'
	commons = []
	for i in b:
		for j in c:
			if i == j:
				commons.append(j)
	print commons 
				

listComprehension()