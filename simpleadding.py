"""given an integer, add all integers from 1 up to that number and 
return that solution"""

def main():
    print simpleAdding(2)
    print simpleAdding(5) 
    print simpleAdding(12)
    print simpleAdding(140)

def simpleAdding(n):    
    sum = 0 
    for i in range(1,n+1):
	    sum += i 
    return sum 
	
main()
"""
#alternate way
def simpleAdding(n):    
    sum = 0 
    for i in range(1,n+1):
	    sum += i 
    return sum 

if __name__ == '__main__':
    print simpleAdding(2)
    print simpleAdding(5) 
    print simpleAdding(12)
    print simpleAdding(140)"""
