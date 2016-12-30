"""determine if a list is already sorted. if not, sort it. 
this cuts down on time complexity"""

def main():
	arr = [1,24,9]
	print shortBubbleSort(arr)
	
def shortBubbleSort(lis):
	swapped = 1
	for i in range(len(lis)):
		if (swapped == 0):
			return;
		for k in range(len(lis)-1,i,-1):
			if (lis[k] < lis[k-1]):
				swap(lis,k, k-1)
				swapped = 1 
	return lis 
def swap(A, x, y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp
	
main()