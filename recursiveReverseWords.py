def main():
    f = open('fun.txt', 'rw')
    allLines = f.readlines() 
    reverse(allLines)

def reverse(lines):
    if len(lines) > 0: 
        line = lines[0] 
        reverse(lines[1:]) 
        print line 
     
main()
