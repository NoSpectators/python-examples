"""this is a sorting algorithm called bubblesort"""

def main():
    array = [BubbleSort([5, 2, 9, 1, 3, 7]),BubbleSort([100,28,9,900]),
			BubbleSort([1,3,2]),BubbleSort([4,3,1])]
    print_results(array)
	
def print_results(arr): #
	for i in arr:
		print "SORTED: " , i 
		
def BubbleSort(A):
    #print "UNSORTED: ", A 
    for i in range(len(A)): #bubble sort goes pair-wise 
		for k in range(len(A)-1,i,-1): 
			if (A[k] < A[k-1]): #keep swapping values from left to right until whole thing is sorted 
				swap(A, k, k-1)	
				print A 
    return A 
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
    
main()