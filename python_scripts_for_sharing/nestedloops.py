def main():
    loops()

def loops():
    space = 10
    for i in range(11): # 10 rows 
        for j in range(space):
            print " ",
        for k in range(0, 2*i-1):
            print "*",
        print "\n"
        space-=1

main()
