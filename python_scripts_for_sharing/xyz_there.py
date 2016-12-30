#return true if given string contains 'xyz' but not preceded by a '.'
def main():
    array = [xyz_there('abcxyz'), xyz_there('abc.xyz'), 
		xyz_there('xyz.abc')]
    print_results(array)

def print_results(arr):
    for i in arr:
	print i 

def xyz_there(str):
    for i in range(len(str)): 
	if str[i] != "." and str[i+1:i+4] == 'xyz':
	    return True
	if str[0:3] == 'xyz':
	    return True
    return False

main()
 
