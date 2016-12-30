def main():

    array = [is_square([[1,8,3],[4,8,6],[7,7,9]]), 
	    is_square([[1,2],[1,2,4]]), 
	    is_square([[5]]),is_square([[1,2],[2,4]])]
    print_results(array)

def print_results(arr):
    for i in arr:
	print i

def is_square(xss):
    rows = len(xss)
    if rows > 0:
	cols = len(xss[0])
	if rows != cols:
	    return False
    	for row in xss:
	    if len(row) != cols:
		return False
	return True
    else:
	return True

main() 
