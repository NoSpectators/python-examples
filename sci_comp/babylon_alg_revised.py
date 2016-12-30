def main():
    babylon()

def babylon():
    a=5
    x=a
    epsilon = 0.001         #initialize termination criterion
    delta = float("inf")    #initialize delta to infinity
    while delta > epsilon:
        xnew = 0.5*(x+5/x)
        delta = abs(xnew-x)
        x=xnew
        print x
    print "the square root of ",a," is ", x
    print "the square root of %d is %.2f" % (a, x)
main() 
