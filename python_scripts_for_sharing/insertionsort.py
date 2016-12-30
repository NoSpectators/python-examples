def main():
    A = [5, 2, 9, 1, 3, 7]

    print "UNSORTED: ",A
    InsertionSort(A)

    print "SORTED: ",A

def InsertionSort(A):
    
    for i in range(1, len(A)):
	
        temp = A[i]

	k = i

	while k > 0 and temp < A[k-1]:

	    A[k] = A[k-1]

	    k-=1
        
        A[k] = temp

    return A

main()