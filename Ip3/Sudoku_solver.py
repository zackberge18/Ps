import random
import pygame
pygame.init()
win=pygame.display.set_mode((540,540))
pygame.display.set_caption("sudoku solver")

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)


#### is valid###3
def is_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return False


#####possible#######
def is_possible(board, pos, n):  ### 4,0
    xpos = pos[0]  # 0
    ypos = pos[1]  # 2
    for i in range(9):
        if board[xpos][i] == n:
            return False
    for i in range(9):
        if board[i][ypos] == n:
            return False
    xpos = (xpos // 3) * 3  # 0
    ypos = (ypos // 3) * 3  # 0
    for i in range(3):
        for j in range(3):
            if board[ypos + j][i + xpos] == n:  # board[1][0]
                return False
    return True



grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
a=1
coords=[]
def number_plate(table):
        global a
        global coords
        for i in range(9):
            for j in range(9):
                text1 = font1.render(str(table[i][j]), 1, (0, 0, 0))
                win.blit(text1, (i * 60 + 10, j * 60 + 10))



def sudoku_plate():
        y4y = 60
        x4x = 60
        for i in range(1, 10):
            if i % 3 == 0:
                if i == 9:
                    pass
                else:
                    pygame.draw.line(win, (255, 0, 255), (10, y4y), (530, y4y),
                                     8)  # line(surface, color, start_pos, end_pos, width) -> Rect
            else:
                pygame.draw.line(win, (255, 0, 255), (10, y4y), (530, y4y),
                                 2)  # line(surface, color, start_pos, end_pos, width) -> Rect
            y4y += 60
            for i in range(1, 10):
                if i % 3 == 0:
                    if i == 9:
                        pass
                    else:
                        pygame.draw.line(win, (255, 0, 255), (x4x, 10), (x4x, 530),
                                         8)  # line(surface, color, start_pos, end_pos, width) -> Rec
                else:
                    pygame.draw.line(win, (255, 0, 255), (x4x, 10), (x4x, 530), 2)
                x4x += 60

            x4x += 60
def Main_draw(board):
        win.fill((200,200,200))
        sudoku_plate()
        number_plate(board)
        pygame.display.update()

run = True


def solve(grid,i,j):
    while grid[i][j]!=0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if is_possible(grid, (i, j), it) == True:
            grid[i][j] = it
            global x, y
            x = i
            y = j
            # white color background\
            win.fill((255, 255, 255))
            sudoku_plate()
            number_plate()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j) == 1:
                return True
            else:
                grid[i][j] = 0
            # white color background\
            win.fill((255, 255, 255))

            sudoku_plate()
            number_plate()
            pygame.display.update()
            pygame.time.delay(50)

while run:

    pygame.time.delay(100)  # how fast game it is gonna be

    for event in pygame.event.get():  # PYGAME
        if event.type == pygame.QUIT:  # SHUT
            run = False  # FUNC

    Main_draw(grid)
pygame.quit()