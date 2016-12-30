"""this is a sorting algorithm called bubblesort"""

"""The bubble sort makes multiple passes through a list. 
It compares adjacent items and exchanges those that are out of order. 
Each pass through the list places the next largest value in its proper place. 
In essence, each item "bubbles" up to the location where it belongs"""

"""This implementation has time complexity O(n^2) """

def main():
	array = [BubbleSort([5, 2, 9, 1, 3, 7]),BubbleSort([100,28,9,900]),
			BubbleSort([1,3,2]),BubbleSort([4,3,1])]
	print_results(array)
	#array = BubbleSort([5,2,9,1,3,7])
	
def print_results(arr): #
	for i in arr:
		print "SORTED: " , i 
		
def BubbleSort(A):
	for i in range(len(A)-1,0,-1): #this provides the 'limit' of j 
		for j in range(i):
			if A[j] > A[j+1]:
				swap(A, j, j+1)	
				#print A 
	return A 
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
    
main()
#idea is to do pairwise sorting
#example: [5,2,9,1,3,7] in the first pass becomes 