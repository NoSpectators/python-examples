def main():
	arr = [isPrime(1), isPrime(2), isPrime(3),isPrime(4), isPrime(5), isPrime(6),isPrime(11)]
	displayResults(arr)
	
def displayResults(array):
	for i in array:
		print i 
	
def isPrime(n):
	if n < 2:
		return False 
	flag = True  
	for i in range(2,n):
		if n % i == 0:
			flag = False  
	return flag 	
	
main()
