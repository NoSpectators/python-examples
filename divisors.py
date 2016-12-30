def divisors():
	num =  int(raw_input('what is your number? '))
	if num ==0:
		print '0'		
	for i in range(1,num+1):
		if num % i == 0:
			print i,'is a divisor'
			
divisors()
		