"""use insertion sort method of sorting to sort a python list"""
"""The insertion sort, although still O(n^2), works in a slightly different way. 
It always MAINTAINS A SORTED SUBLIST IN THE LOWER POSITIONS OF THE LIST. 
Each new item is then "inserted" back into the previous sublist such that 
the sorted sublist is one item larger."""

def main():
    A = [5, 2, 9, 1, 3, 7]
    print "UNSORTED: ",A
    InsertionSort(A)
    print "SORTED: ",A

def InsertionSort(A):    
	for i in range(1, len(A)):	
		temp = A[i] #temp is current value 
		k = i #k is the position 
		while k > 0 and temp < A[k-1]:
			A[k] = A[k-1]
			k-=1        
		A[k] = temp
		#print A 
	return A

main()

#example: [5,2,9,1,3,7]
#starts at position 1, which is 2. it sorts from index 0-1,
#which produces [2,5,9,1,3,7] 
#then it considers indices 0-2
#so the list becomes [2,5,9
#then list becomes [1,2,5,9,3,7]
#then list becomes [1,2,3,5,9,7]
#finally it becomes [1,2,3,5,7,9]