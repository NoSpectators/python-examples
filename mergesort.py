def main():
    A = [5, 2, 9, 1, 3, 7]
    print "UNSORTED: ",A

    MergeSort(A)
    print "SORTED: ",A

def MergeSort(A):  

	if len(A) > 1: 	

		mid = len(A)/2	
		left_half = A[:mid]	
		right_half= A[mid:]
	
		MergeSort(left_half)	
		MergeSort(right_half)

		i = j = k = 0

		while i < len(left_half) and j < len(right_half):     		
			if left_half[i] < right_half[j]:
				A[k] = left_half[i]		
				i += 1	    
			else:		
				A[k] = right_half[j]
				j += 1	  
			k += 1	
	
		while i < len(left_half):
			A[k] = left_half[i]
			i += 1		    
			k+=1	

		while j < len(right_half):
			A[k] = right_half[j]		
			j += 1		   
			k += 1

	return A

main()

