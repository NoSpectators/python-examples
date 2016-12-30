def main():
    nums = [2, 1, 2, 3, 4]
    print  "there are",count_evens(nums),"even nums in array." 

def count_evens(arr):
    count = 0
    for i in arr:
        if i % 2 == 0:
	    count += 1
    return count

main()
