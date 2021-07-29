import random
import pygame
pygame.init()
win=pygame.display.set_mode((600,600))
pygame.display.set_caption("PAcman Fake")



class MyPlayer(object):  # PLAYER CLASS

    def __init__(self,width,height):
        self.x = 80
        self.y=80
        self.height=height
        self.width=width
        self.vel=5
        self.my_Score=0
    def draw(self):
        font = pygame.font.SysFont("comicsans", 30, True)
        # This should go inside the redrawGameWindow function
        text = font.render("Score: " + str(self.my_Score), 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color

        win.blit(text, (390, 10))


        pygame.draw.rect(win, (255, 255, 0), (self.x, self.y, self.width,self.height)) #PLAYER SQUARE

class MyStar(object): # PEARL CLASS
    def __init__(self,width,height):
        self.x = 237 # TO RANDOMLY SHOW AFTER EACH TIME YOU EAT THE PEARL
        self.y =432  # TO RANDOMLY SHOW AFTER EACH TIME YOU EAT THE PEARL
        self.height = height
        self.width = width
        self.eat=False



    def draw(self):
        if self.eat==False:
            pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width / 2, self.height / 2))
            enemy.draw()
        if self.eat==True:
            self.x=random.randint(0,500) # TO RANDOMLY SHOW AFTER EACH TIME YOU EAT THE PEARL
            self.y=random.randint(0, 500) ## TO RANDOMLY SHOW AFTER EACH TIME YOU EAT THE PEARL
            enemy.draw()


class MyEnemy(object):

    def __init__(self, width, height):
        self.x = 50  # TO RANDOMLY SHOW AFTER EACH TIME YOU EAT THE PEARL
        self.y = 79  # TO RANDOMLY SHOW AFTER EACH TIME YOU EAT THE PEARL
        self.height = height
        self.width = width


    def draw(self):
        if star.eat == False:
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width / 2, self.height / 2))

        if star.eat == True:
            self.x = random.randint(0, 600)  # TO RANDOMLY SHOW AFTER EACH TIME YOU EAT THE PEARL
            self.y = random.randint(0, 600)  ## TO RANDOMLY SHOW AFTER EACH TIME YOU EAT THE PEARL
            star.eat = False
def draw():

        win.fill((128,0,128))

        star.draw()


        enemy.draw()
        player.draw()

        pygame.display.update()




player=MyPlayer(60,60) # PLAYER(x,y,widht,height)
star=MyStar(30,30)     # PEARL(width,height)
enemy=MyEnemy(30,30)     #Enemy Pearl

run= True
while run:


    pygame.time.delay(30)# how fast game it is gonna be
    
    for event in pygame.event.get():     #PYGAME
        if event.type == pygame.QUIT:    #SHUT
            run=False                    #FUNC


    ################KEYS################
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:# LEFT KEY
        player.x-=player.vel #SPEED
    if keys[pygame.K_RIGHT]:#RIGHT KEY
        player.x +=player.vel #SPEED
    if keys[pygame.K_UP]:# UP KEY
        player.y-=player.vel #SPEED
    if keys[pygame.K_DOWN]: #DOWN KEY
        player.y+=player.vel #SPEED

    #### GO BIGGER ## EVERY TIME YOU EAT A SQUARE
    # IF YOU EAT THE SMALL SQUARE YOU CAN EXPAND
    height_dif=player.height - star.height
    width_dif=player.width - star.width
    im_y0 = star.y - (height_dif)
    im_x0 = star.x - (width_dif)
    im_y1 = star.y + (height_dif)
    im_x1 = star.x + (width_dif)
    #######################################################
    #########################
    ################       FOR ENEMY   ##########

    height_dif = player.height - enemy.height
    width_dif = player.width - enemy.width
    em_y0 = enemy.y - (height_dif)
    em_x0 =enemy.x - (width_dif)
    em_y1 = enemy.y + (height_dif)
    em_x1 = enemy.x + (width_dif)

    if star.eat==False:
        # if player.x>star.x - (player.width - star.width) and player.x<star.x + (player.width - star.width):
        #     if player.y >star.y - (player.height - star.height) and player.y < star.y + (player.height - star.height):
         if player.x>im_x0 and player.x<im_x1:
             if player.y >im_y0 and player.y < im_y1:
                player.my_Score+=1
                player.width += 4
                player.height+= 4
                print("hello world")
                #every time this if is true dissapper star
                star.eat=True
         if player.x > em_x0 and player.x < em_x1:
            if player.y > em_y0 and player.y < em_y1:
                player.my_Score -= 1
                player.width -= 4
                player.height -= 4



    #MAIN DRAW FUNC
    draw()


    
    
    
pygame.quit()