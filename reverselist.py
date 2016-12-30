def main():
    arr = [reverse_list([1,2,3,4]),reverse_list([5,11,9]), \
            reverse_list([7,0,0])]
    print_results(arr)

def print_results(arr):
    for i in arr:
	print 'the reversed list is',i

def reverse_list(nums):
    length = len(nums)
    new_list = [None]*length
    for i in nums:
	length -= 1
	new_list[length] = i
    return new_list

main()


