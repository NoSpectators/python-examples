def twoElementsSumKBruteForce(A,K):
    n = len(A)
    for i in range(0,n):
	for j in range(i+1, n):
	    if (A[i] + A[j] == K):
		print "item ", A[i] , "and item " , A[j], " sum to " , K
		return 1
            else:
		print "no numbers sum to K" 
                return 0

def SelectionSort( A ):
    for i in range(len(A)):
        least = i
        for k in range(i+1, len(A)):
            if A[k] < A[least]:
                least = k
        swap(A, least, i)

def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


A = [1, 4, 45, 6, 10, -8]
SelectionSort(A) 
twoElementsSumKBruteForce(A, 111)
A = [1, 4, 6]
SelectionSort(A)
twoElementsSumKBruteForce(A, 5)
A = [1, 8, 7]
twoElementsSumKBruteForce(A, 8)
SelectionSort(A)
twoElementsSumKBruteForce(A, 8) 
