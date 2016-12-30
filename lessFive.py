def lessFive():
	arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	lis = []
	for i in arr:
		if i < 5:
			lis.append(i)
	print lis 
	
lessFive()