# recursive binary search algorithm

def main():
	A = [534, 236, 277, 454, 676, 989]
	print BinarySearchRecursive(A, 277)

def BinarySearchRecursive(numList, value, low= 0, high = -1):
	if not numList: return -1
	if high==-1: high = len(numList)-1
	if low == high:
		if numList[low] == value: return low
		else: return -1
	mid = low + (high-low)//2
	if numList[mid] > value:
		return BinarySearchRecursive(numList, value, low, mid-1)
	elif numList[mid] < value: 
		return BinarySearchRecursive(numList, value, mid+1, high)
	else:
		return "value of num is at index " + str(mid)


main()
