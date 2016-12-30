#prints a 2D array numbered num through n*n with n rows and n cols

def main():
    print '2x3 matrix =',array(2,3)
    print '1x2 matrix =',array(1,2)
    print '3x5 matrix =',array(3,5)

def array(rows,cols):
    board = []
    num = 1
    for i in range(rows):
        board.append([])
        for j in range(cols):
            board[i].append(num)
            num+=1
    return board

main()

