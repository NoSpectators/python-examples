"""given an array, check if there are repeats, if so, which one repeats 
the most"""

def main():
	array = [num_most_repeated([3, 2, 1, 2, 2, 3]),num_most_repeated([3, 3, 3, 2, 2, 3]),
				num_most_repeated([1,2,4]),num_most_repeated([4,4,4,5])]
	print_results(array)
	
def print_results(arr):
	for i in arr:
		print i 

def num_most_repeated(arr):
	counter = maxCounter = 0
	candidate = arr[0]
	for i in range(len(arr)):
		counter = 1
		for j in range(i+1, len(arr)):
			if (arr[i]==arr[j]): #INNER LOOP  
				counter += 1	#if a duplicate exists, maxCounter will go to at least 2
		if (counter > maxCounter): #OUTER LOOP updates 
			maxCounter = counter  #maxCounter and candidate 
			candidate = arr[i]
	if maxCounter == 1: #final check at end 
		return "sorry no duplicates"
	return str(candidate) + " appeared " + str(maxCounter) + " times"
main()
