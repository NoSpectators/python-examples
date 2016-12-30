"""check which if there are duplicates in an array"""

def main():
	array = [CheckDuplicatesBruteForce([3, 2, 10, 20, 22, 32]), 
			CheckDuplicatesBruteForce([3, 2, 1, 2, 2, 3])]
	print_results(array)
	
def print_results(arr):
	for i in arr:
		print i
	
def CheckDuplicatesBruteForce( A ):
	for i in range(len(A)):
		for j in range(i+1, len(A)):
			if (A[i] == A[j]):
				print "Duplicates exist:", A[i]
				return; #only way to break out of the inner loop here 
	return "No duplicates in given array."

main()