# import numpy as np
#
# board = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]
#
#
#
# #### is valid###3
# def is_empty(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j]==0:
#                 return  (i,j)
#     return False
#
# #####possible#######
# def is_possible(board,pos,n): ### 4,0
#     xpos=pos[0] #4
#     ypos=pos[1] #0
#     for i in range(9):
#        if  board[xpos][i]==n:
#            return False
#     for i in range(9):
#         if board[i][ypos]==n:
#             return False
#     xpos=(xpos//3)*3 #1
#     ypos=(ypos//3)*3 #0
#     for i in range(3):
#         for j in range(3):
#           if board[ypos+j][i+xpos]==n: # board[1][0]
#             return False
#     return True


# #### to solve solution
# def solve_puzzle(su_board):
#     find=is_empty(su_board)
#     if find==False:
#         return True
#     else:
#         x,y=find
#
#     for i in range(1,10):
#         if is_possible(su_board,(x,y),i):
#             print(i)
#             su_board[x][y] = i
#             print(su_board)
#

            if solve_puzzle(su_board):
                return True

            su_board[x][y]=0
    return False

            

    
    
