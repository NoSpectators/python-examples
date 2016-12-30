#return mean average of array ignoring smallest and largest values of array

def main():
    arr = [centered_average([1,2,3,4,100]),centered_average([1,1,5,5,10,8,7]),
	centered_average([-10,-4,-2,-4,-2,0])]
    print_results(arr)

def print_results(arr):
    for i in arr:
		print 'centered average is',i

def centered_average(array):
	"""this is how i would teach this problem to newbies """
	total = 0
	min = array[0]
	max = array[0] 
	for i in array:	
		total += i  #gets total 
		if i < min: #gets min value 
			min = i
		if i > max:  #gets max value 
			max = i	
	return (total-max-min)/(len(array)-2)
	"""this is the very easy way to do it"""
	#return (sum(array)-max(array)-min(array))/(len(array)-2) 

main()
 
