''' write a for loop that produces the following output:
  
1 4 9 16 25 36 49 64 81 100

''' 

def main():
    loopsquares()

def loopsquares():
    for i in range(1,11):
        print str(i*i) + " ",
main()
