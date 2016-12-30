#return true if first or last num in array is a 6

def main():
    array = [first_last6([1,2,6]),first_last6([6,1,2,3]),first_last6([13,6,1])]
    print_results(array)

def print_results(array):
    for i in array:
  	print 'it is',i,'that 6 is either first or last in the array'

def first_last6(arr):
    return arr[0] == 6 or arr[-1] == 6

main()


