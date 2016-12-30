def CheckDuplicatesSorting(A):
    A.sort()
    for i in range(0, len(A)-1):
	for j in range(i+1, len(A)):
	    if (A[i] == A[i+1]):
		print ("Duplicates exist:"), A[i]
		return;
    print("No duplicates in given array.")

A = [33, 2, 10, 20, 22, 32]
CheckDuplicatesSorting(A)
A = [4, 2, 1, 3, 2, 4]
CheckDuplicatesSorting(A)

