def main():
    A = [5, 2, 9, 1, 3, 7]

    print "UNSORTED: ",A

    QuickSort(A,0,len(A)-1)
    print "SORTED: ",A

def QuickSort(A, low, high):
    if low < high:
	pivot = Partition(A,low,high)
	QuickSort(A,low,pivot-1)
	QuickSort(A,pivot+1,high)

def Partition(A,low,high):
    pivot = low
    swap (A, pivot, high)
    for i in range(low,high):
	if A[i] <= A[high]:
	    swap (A,i,low)
	    low +=1
    swap(A, low, high)
    return low

def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

main()