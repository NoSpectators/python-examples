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
A = [1, 4, 45, 6, 10, -8]
A.sort()
twoElementsSumKBruteForce(A, 111)
A = [1, 4, 6]
A.sort()
twoElementsSumKBruteForce(A, 5)
A = [1, 8, 7]
twoElementsSumKBruteForce(A, 8)
A.sort()
twoElementsSumKBruteForce(A, 8) 
