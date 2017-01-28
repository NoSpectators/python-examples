# iterative binary search algorithm

def main():
	A = [534, 236, 277, 454, 676, 989]
	print BinarySearchIterative(A, 277)

def BinarySearchIterative(numList, value):
	low = 0
	high = len(numList)-1
	while low <= high:
		mid = (low+high)//2
		if numList[mid] > value: high = mid-1
		elif numList[mid] < value: low = mid+1
		else: return "value of num is at index " + str(mid)
	return -1

main()
