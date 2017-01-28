def main():
	A = [34, 46, 78, 99, 189, 345, 567]
	print OrderedLinearSearch(A, 189)

def OrderedLinearSearch(numList, value):
	for i in range(len(numList)):
		if numList[i] == value:
			return "value found at index " + str(i)
		elif numList[i] > value:
			return -1
	return -1 

main()