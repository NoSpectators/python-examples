def main():

    array = [no_teen_sum(1,2,3), no_teen_sum(2,13,1), no_teen_sum(2,1,14)] 
    print_results(array)

def print_results(arr):
    for i in arr:
        print 'the sum of the array (excluding teens) except 15 and 16 is', i

def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in range(13,20):
        if n in range(15,17):
	    return n
        return 0
    return n

main()
  
