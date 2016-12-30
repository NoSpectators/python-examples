def removeAdjacentRepeats(arr):
    i = 1
    while i < len(arr):
        if (arr[i] == arr[i-1]):
	    arr.pop(i)
	    i -= 1
	i += 1
    return arr

arr = ["A", "B", "C", "C", "C", "C", "B", "A"]
print removeAdjacentRepeats(arr)

