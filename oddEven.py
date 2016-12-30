def numOddEven():
	num = int(raw_input('please enter a number:' ))
	if num % 2 == 0 and num % 4 != 0:
		return 'even and not a multiple of 4'
	elif num % 2 == 0:
		return 'even and multiple of 4'
	return 'odd'

print numOddEven()