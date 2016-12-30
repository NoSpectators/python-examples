"""return the difference of largest/smallest int in given array """

def main():
    arr = [big_diff([10,3,5,6]), big_diff([7,2,10,9]), big_diff([2,10,7,2])]
    print_results(arr)

def print_results(arr):
    for i in arr:
    	print 'difference =',i

def big_diff(nums):
    return max(nums)-min(nums) #this is cheating :o) 
    """min = nums[0]
    max = nums[0]
    for i in nums:
	if i < min:
	    min = i
    for i in nums:
	if i > max:
	    max = i
    return max - min"""

main()

