def main():
	A = [44, 33, 545, 9, 2,545, 99, -123]
	print majorityElement(A)

def majorityElement(numList):
	d = {}
	for i in numList:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	maximum = max(d, key=d.get)
	return "the majority element is " + str(maximum)

main()