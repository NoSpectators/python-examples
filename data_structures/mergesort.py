"""Merge sort is a recursive algorithm that continually splits a list in half. 
If the list is empty or has one item, it is sorted by definition (the base case).
 If the list has more than one item, we split the list and recursively invoke a 
 merge sort on both halves. Once the two halves are sorted, the fundamental 
 operation, called a merge, is performed."""
 
 """this algorithm is also used for sorting a linked list"""

def main():
    A = [5, 2, 9, 1, 3, 7]
    print "UNSORTED: ",A
    MergeSort(A)
    print "SORTED: ",A
	
def MergeSort(A):    
    if len(A) > 1: 	
    	mid = len(A)/2	
    	left_half = A[:mid]	#left half 
    	right_half= A[mid:]	#right half 
    	MergeSort(left_half) #call recursive function on each half 
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

