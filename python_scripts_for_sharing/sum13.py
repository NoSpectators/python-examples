#return the sum of the numbers in the array except
#do not count 13 or numbers immediately after 13

def main():
    array = [sum13([1,2,2,1]),sum13([1,1]),sum13([1,2,2,1,13]),sum13([1,13,1])]
    print_results(array)

def print_results(arr):
    for i in arr:
        print 'the sum without 13 is',i

def sum13(nums):
    if len(nums) == 0:
	return 0
    for i in range(len(nums)):
	if nums[i] == 13:
	    nums[i] = 0
	    if i+1 < len(nums):
	        nums[i+1] = 0
    return sum(nums)

main()
