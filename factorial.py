"""given an integer, return the factorial of it """

def main():
    print '1 factorial = ',factorial(1)
    print '2 factorial = ',factorial(2)
    print '3 factorial = ',factorial(3)
    print '4 factorial = ',factorial(4)
	
def factorial(num):
	factorial = 1
	while num >= 1:
		factorial *= num 
		num -= 1
	return factorial

main()
		