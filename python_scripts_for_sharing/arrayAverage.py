"""take any array, return the average of the nums"""
def main():
    bigarray = [average([1,-2,4]),average([1,2,3,4,5]),average([9,1,3.5]),average([])] 
    print_results(bigarray)

def print_results(arr): #prints results from multiple examples in main 
    for i in range(len(arr)):
        print 'array',i+1,'average is',arr[i]
    
def average(array):
    if (len(array)) == 0:
		return "0.00"
    sum = 0 
    count = 0 
    for i in array:
        sum += i 
        count+=1
    return ("%.2f" % (sum / count)) #returns the float average 

main() 
