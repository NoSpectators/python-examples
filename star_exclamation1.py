
#prints 2 rows of stars and asterisks

def starloop():
    for i in range(1, 3):
        for j in range(1, 4):
	    for k in range(1, 5):
		print '*',
	    print '!',
        print "\n"

def main():
    starloop()

main()
