def valid(board,r,c,no):
    if no in board[r]:
        return False
    if any(board[i][c]==no for i in range(0,9)):
        return False
    br,bc=3*(r//3),3*(c//3)
    for i in range(br,br+3):
        for j in range(bc,bc+3):
            if board[i][j]==no:
                return False
    return True
def func(pos,board):
    r,c=pos
    
    while board[r][c]!=".":
        c+=1
        if c==9:
            c=0
            r+=1
        if r==9:
            return True
    print(board[r][c])
    for i in range(1,10):
        if valid(board,r,c,str(i)):
            board[r][c]=str(i)
            if func((r,c),board):
                return True
    board[r][c]='.'
    return False

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

func((0,0),board)
for i in board:
    print(i)