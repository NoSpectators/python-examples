def main():
    array = [diagonal_vals([[1,8,3],[4,8,6],[7,7,9]]), 
		diagonal_vals([[1,2,3],[4,5]])]
    print_results(array)

def print_results(arr):
    for i in arr:
	if i == None:
	    print 'None'
	else:
	    print 'the diagonal vals are',i

def diagonal_vals(xss):
    #check if xss is square
    if is_square(xss):
	i = 0
	diagonal_vals = []

        #checks each row using i to get diagonal value
	for row in xss:
	    diagonal_vals.append(row[i])
	    #since i increments, it goes to next 'spot' in the row for each row
	    i += 1
 	return diagonal_vals  
    else:
	return None

def is_square(xss):
    rows = len(xss)
    if rows > 0:
	cols = len(xss[0])
        # compare rows to cols length
	if rows != cols:
	    return False
	#now iterate
	for row in xss:
	    if len(row) != cols:
		return False
	return True
    else:
	return True

main()
     
