def main():
	A = [534, 246, 78, 987, -18, 6,99]
	print UnOrderedLinearSearch(A, 987)

def UnOrderedLinearSearch(numList, value):
	for i in range(len(numList)):
		if numList[i] == value:
			return "value found at index " + str(i)
	return -1

main()