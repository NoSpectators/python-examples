def main():
    writeStars2(1)
    writeStars2(2)
    writeStars2(3)
    writeStars2(4)
    writeStars2(5)

def writeStars2(n):
    if n == 0:
        print ""
    else: 
        print "*", 
        writeStars2(n-1)

main() 

