def listOverlap():
	a = int(raw_input("what size do you want list 1? "))
	A = []
	for i in range(a):
		num = int(raw_input("Enter a num: "))
		A.append(num)
	b = int(raw_input("what size do you want list 2? "))
	B = []
	for i in range(b):
		num = int(raw_input("Enter a num: "))
		B.append(num)
		
	
	new_lis = []
	for num in A:
		if num in new_lis:
			None 
		elif num in B:
			new_lis.append(num)
	if len(new_lis) == 0:
		print 'no common numbers'
	else:
		print 'common numbers are',new_lis
listOverlap()
				
	