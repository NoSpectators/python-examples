def main():
    A = [5, 2, 9, 1, 3, 7]

    print "UNSORTED: ",A

    ShellSort(A)
    print "SORTED: ",A

def ShellSort(A):
    sublistcount = len(A)//2
    while sublistcount > 0:
	for startposition in range(sublistcount):
	    GapInsertionSort(A, startposition, sublistcount)
	print("After increments of size",sublistcount,"The list is",A)
	sublistcount = sublistcount // 2

def GapInsertionSort(A, start, gap):
    for i in range(start+gap,len(A),gap):
	currentvalue = A[i]
	position = i
	
	while position >= gap and A[position-gap] > currentvalue:
	    A[position] = A[position-gap]
	    position = position-gap
	
	A[position] = currentvalue
    return A

main()