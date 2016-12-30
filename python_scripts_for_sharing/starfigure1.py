def main():
    starfigure1()

def starfigure1():
    for i in range(1, 6):
        for j in range(1, -4*i+21, 1):
            print "/",
        for k in range(1, 8 *i-8+1, 1):
	    print "*", 
	for j in range(1, -4*i+21, 1):
	    print "\\", 
	print ""

main()
