def mystery1(n):
    if (n <= 1):
	print n, 
    else:
        mystery1(n / 2)
        print ", " + str(n),

def main():
    mystery1(1)
    print ""
    mystery1(2)
    print ""
    mystery1(16)
    print ""
main()
