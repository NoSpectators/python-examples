def main():
    array = [gcd(3,12),gcd(15,10),gcd(0,6),gcd(25,5),gcd(30,900)] 
    print 'the gcd\'s are',array

def gcd(a,b):
    if a == 0:
	return b
    if b == 0:
	return a
    if a!=b:
	a_divisors=[]
	b_divisors=[]
	for i in range(1,a+1):
	    if a%i == 0:
 		a_divisors.append(i) 
	    if b % i == 0:
		b_divisors.append(i)
	shared_divisors = []
	for i in a_divisors:
	    if i in b_divisors:
		shared_divisors.append(i)
	#find max divisor in shared list
	max_divisor = shared_divisors[0]
	for i in shared_divisors:	
	    if i > max_divisor:
		max_divisor = i
	return max_divisor
main()
 
		 
