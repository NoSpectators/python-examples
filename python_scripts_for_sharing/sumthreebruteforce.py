def threeElementsSumKBruteForce(A, K):
    n = len(A)
    for i in range(0, n-2):
        for j in range(i+1, n-1):
	    for k in range(j+1, n):
		if (A[i] + A[j] + A[k] == K):
		    print "yes-->", A[i],"+",A[j],"+",A[k],"=", K 
		    return 1 
            	    
    print "there are not 3 nums who's sum is K"
    return 0
A = [1, 6, 45, 4, 10, 18]
A.sort()
threeElementsSumKBruteForce(A, 11) 
threeElementsSumKBruteForce(A, 12)
  
