import pygame,sys
import numpy as np

pygame.init()

WIDTH=600
HEIGHT=600
LINE_WIDTH=15
CIRCLE_RADIUS=50
CIRCLE_WIDTH=10
#rgb colors
RED=(255,0,0)
BG_COLOR=(28,170,156)
LINE_COLOR=(23,145,135)

#Board
board=np.zeros((3,3))
#print(board)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill( BG_COLOR )


def check(board, row, col):
    if board[row][0] == board[row][1] == board[row][2] == 1:
        print(f"winner is 1")
    elif board[row][0] == board[row][2] == board[row][2] == 2:
        print(f"winner is 1")
    elif board[0][0] == board[1][1] == board[2][2] == 1:
        print(f"winner is 1")
    elif board[0][0] == board[1][1] == board[2][2] == 1:
        print(f"winner is1")
    elif board[0][2] == board[1][1] == board[2][0] == 2:

        print(f"winner is 2")
    try:
        if board[row][col] == board[row+1][col] == board[row+2][col] == 1:
            print(f"winner is1 side")
        elif  board[row][col] == board[row+1][col] == board[row+2][col] == 2:
            print(f"winner is 2 side")
    except :
        pass

def draw_lines():
    pygame.draw.line(screen,LINE_COLOR,(5,200),(595,200),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(5,400),(595,400),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(200,5),(200,595),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(400,5),(400,595),LINE_WIDTH)
def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col]==1:
                pygame.draw.circle(screen,RED,(int(col*200+200/2),int(row*200+200/2)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col]==2:
                #line(surface, color, start_pos, end_pos, width)
                #lines(surface, color, closed, points) -> Rect
                pygame.draw.line(screen,(128,128,128),(col*200+50,row*200+50),(col*200+200-50,row*200+200-50),20)
                pygame.draw.line(screen,(128,128,128),(col*200+200-50,row*200+50),(col*200+50,row*200+200-50),20)
            check(board, row, col)

def mark_square(row,col,player):
        if board[row][col]!=0:
          pass
        else:
            board[row][col]=player



def available_square(row,col):
        return board[row][col]==0
draw_lines()

player=1
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouseX=event.pos[0]
            mouseY=event.pos[1]


            #print(mouseX, mouseY)

            clicked_row=int(mouseY) // 200

            clicked_col=int(mouseX) // 200

            #print(clicked_col,clicked_row)

            if player==1:

                mark_square(clicked_row,clicked_col,1)


                player=2
            elif player==2:
                mark_square(clicked_row, clicked_col, 2)


                player = 1
            draw_figures()



            print(board)
    pygame.display.update()