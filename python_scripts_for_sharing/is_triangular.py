def main():
    array = [is_triangular([[5,0,0],[6,3,0],[7,8,9]]), 
	is_triangular([[1,0,0,0],[2,2,0,0],[3,3,3,0],[4,4,4,4]]),
	is_triangular([[1,0,1],[0,0,0],[0,1,1]])] 
    print_results(array)

def print_results(arr):
    for i in arr:
	print i

def is_triangular(xss):
    if is_square(xss) == True:
	illegal_above_diagonal = False
	illegal_below_diagonal = True

        for i in range(len(xss)):
  	    for j in range(len(xss)):

	        illegal_above_diagonal = illegal_above_diagonal or \
	        (checkRow(i,j)== "above" and xss[i][j] != 0)
	        illegal_below_diagonal = illegal_below_diagonal or \
        	(checkRow(i,j)== "below" and xss[i][j] != 0)
 
                if illegal_above_diagonal and illegal_below_diagonal:
		    return False
        return True
    return False

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

def checkRow(i,j):
    if i == j:
	return "diagonal"
    if i > j:
	return "below"
    return "above"

main()
    
   
