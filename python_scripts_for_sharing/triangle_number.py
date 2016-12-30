def main():
    print triangle_number(0)
    print triangle_number(1)
    print triangle_number(11)
    print triangle_number(5)
    print triangle_number(100)

def triangle_number(n):
    num = 0
    count = 0
    while count <= n:
        num+=1
	count+=num
        if n == 0:
            return 0
        else:
            if count == n:
	        return num
                break
	    if count > n:
	        return num

main()

