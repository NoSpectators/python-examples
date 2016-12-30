def main ():
    array = [subsequence_index([2,3,4], [5,4,3,2,1]),
		subsequence_index([5,6,7],[1,2,3,5,6,7]),
		subsequence_index([1,2,3],[3,4,5,6,1,2,3])]
    print_results(array)

def print_results(arr):
    for i in arr:
        print 'xs is also in ys at element',i

def subsequence_index(xs, ys):
    xs_index = -1
    for i in range(len(ys)):
	    if xs[0] == ys[i]:
	        xs_index = i
	        sub_string = True

	    for j in range(len(xs)):
    	 	if xs[j] != ys[i+j]:
    		    sub_string = False
    	  	    break
		if sub_string == True:
			return xs_index
    else:
        xs_index = -1
        return None

main()
