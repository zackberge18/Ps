import numpy as np

board=np.zeros((3,3))
print(board)
print(board.shape)

rows=board.shape[0]
cols=board.shape[1]

def check(board,row,col):
             if board[row][0]==board[row][1]==board[row][2]==1:
                 print(f"winner is 1")
             elif board[row][0]==board[row][2]==board[row][2]==2:
                 print(f"winner is 1")
             if board[0][0]==board[1][1]==board[2][2]==1:
                 print(f"winner is 1")
             elif board[0][0]==board[1][1]==board[2][2]==1:
                 print(f"winner is1")
             elif board[0][2]==board[1][1]==board[2][0]==2:

                 print(f"winner is 2")
             if  board[0][col]==board[1][col]==board[2][col]==1:
                 print(f"winner is1")
             if  board[0][col]==board[1][col]==board[2][col]==1:
                 print(f"winner is 2")

while True:

    for row in range(rows):
        for col in range(cols):
            number=input("1 or 2")
            board[row][col]=int(number)
            print(board)
            check(board,row,col)


