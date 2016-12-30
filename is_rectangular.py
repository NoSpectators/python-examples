def main():
    array = [is_rect([[1,2,3],[4,5,6]]), is_rect([[1,2,3,4],[1,2]]),
		is_rect([[]]), is_rect([[True],[False]])]
    print_results(array)

def print_results(arr):
    for i in arr:
	if i == True:
	    print 'is rectangular'
        else:
	    print 'not rectangular'

def is_rect(xss):
    if len(xss) == 0:
	return True
    standard = len(xss[0])
    for i in xss:
	if len(i) != standard:
	    return False
    return True

main()

