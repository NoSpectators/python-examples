#return the sum of nums in array except ignore sections of numbers
#between starting with 6 and extending to the next 7
#return 0 for no nums

def main():
    arr = [sum67([1,2,2]), sum67([1,2,2,6,99,99,7]),sum67([1,1,6,7,2])]
    print_results(arr)

def print_results(arr):
    for i in arr:
	print 'sum of array (omitting 6 thru 7) is',i

def sum67(nums):
    for i in range(len(nums)):
        if nums[i] == 6:
	    nums[i] = 0
	    for j in range(i+1,len(nums)):
		temp = nums[j]
		nums[j] = 0
		if temp == 7:
		    i = j+1
		    break
    return sum(nums)

main()
	
