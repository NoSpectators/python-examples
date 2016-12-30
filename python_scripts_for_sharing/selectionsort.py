
def main():
    A = [5, 2, 9, 1, 11, 0, 67]

    print "UNSORTED: ",A
    SelectionSort(A)

    print "SORTED: ",A

def SelectionSort( A ):
    
    for i in range(len(A)):
        
        least = i
        
        for k in range(i+1, len(A)):
 
           if A[k] < A[least]:

		least = k
	
        swap(A, least, i)



def swap(A, x, y):
    
    temp = A[x]
    
    A[x] = A[y]
    
    A[y] = temp


    
main()