#prints a 2D array numbered num through n*n with n rows and n cols

def main():
    print 'n x n matrix =',array(3)

def array(n):
    board = []
    num = 1
    for i in range(n):
        board.append([])
        for j in range(n):
	    board[i].append(num)
	    num+=1
    return board

main() 
