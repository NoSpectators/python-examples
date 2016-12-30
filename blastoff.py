"""just print 5,4,3,2,1 blastoff! """
def main():
    blastoff()

def blastoff():

    print 'T-minus'
    for i in range(5, 0, -1):
       	print str(i) + ","
    print 'Blastoff!'

main()
