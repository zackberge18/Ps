import pygame
pygame.init()
WIDTH=1200
HEIGHT=900
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First GAme")

# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
n_left=[pygame.image.load("1.png"),pygame.image.load("2.png"),pygame.image.load("3.png"),pygame.image.load("4.png"),pygame.image.load("5.png"),pygame.image.load("6.png")]
n_right=[pygame.image.load("1 (2).png"),pygame.image.load("2 (2).png"),pygame.image.load("3 (2).png"),pygame.image.load("4 (2).png"),pygame.image.load("5 (2).png"),pygame.image.load("6 (2).png")]
bg = pygame.image.load('bg1.jpg')
char = pygame.image.load('standing.png')
clock=pygame.time.Clock()
chars=[walkRight,walkLeft,n_right,n_left]
shuriken=pygame.image.load("arrow.png")
bulletSound=pygame.mixer.Sound("bullet.mp3")

hitSound=pygame.mixer.Sound("hit.mp3")
music=pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
score=0
class Player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0
        self.standing=True
        self.facing=0
        self.hitbox=(self.x+20,self.y,200,400)
    def class_draw(self,win):
        if self.walkCount + 1 > 18:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(chars[2][self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(chars[3][self.walkCount // 3],(self.x, self.y))
                self.walkCount += 1
            else:
                if self.right:
                    win.blit(chars[3][self.walkCount // 3], (self.x, self.y))
                else:
                    win.blit(chars[2][self.walkCount // 3], (self.x, self.y))


        else:
            if self.facing==0:
                    win.blit(chars[3][1], (self.x, self.y))
            else:
                      win.blit(chars[2][0], (self.x, self.y))
            self.hitbox = (self.x + 20, self.y, 200, 400)
            pygame.draw.rect(win, (255,0,0), self.hitbox,4)

class projectile(object):
    def __init__(self,x,y,facing):
        self.x=x
        self.y=y
        self.facing=facing
        self.vel=8*facing

    def p_draw(self,win):
        win.blit(shuriken, (int(self.x+50), int(self.y+self.y/4)))


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount=0
        self.vel=3
        self.path = [x, end]  # This will define where our enemy starts and finishes th
        self.hitbox = (self.x + 20, self.y-100, 64, 200)
        self.health=10
        self.visible=True
    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount+1 >=33:
                self.walkCount=0
            if self.vel>0:
                win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            else:
                win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 20, self.y-100, 64, 200)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,4)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50-(5*(10-self.health)), 10))


    def move(self):
        if self.vel>0:
            if self.x+self.vel<self.path[1]:
                self.x +=self.vel
            else:
                self.vel=self.vel*-1
                self.walkCount=0
        else:
            if self.x-self.vel>self.path[0]:
                self.x +=self.vel
            else:
                self.vel =self.vel *-1
                self.walkCount=0
    def hit(self):
        hitSound.play()
        print("hit")
        self.health-=1
        if self.health==0:
            self.visible=False



def draw():
    global walkCount

    win.blit(bg, (0, 0))
    for bullet in bullets:
        bullet.p_draw(win)
       # print(bullet.p_draw)
    text=font.render("Score :"+ str(score),1,(0,0,0))
    win.blit(text,(1000,50))
    man.class_draw(win)
    goblin.draw(win)
    pygame.draw.rect(win, (255, 0, 0), (600, 800, 300, 100), 10)

    pygame.display.update()
#mainloop
man =Player(900,600,200,350)
goblin=enemy(500,830,64,100,900)
run=True
bullets=[]
font=pygame.font.SysFont("comicsans", 30,True)
while run:
    man.left = False
    man.right = False
    man.standing=True
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    for bullet in bullets:
        # if bullet.y>goblin.hitbox[1]+goblin.hitbox[3] and bullet.y>goblin.hitbox[1]:

            if bullet.x>goblin.hitbox[0] and bullet.x<goblin.hitbox[0]+goblin.hitbox[2]:
                if goblin.visible:
                    goblin.hit()
                    score +=1
                bullets.pop(bullets.index(bullet))
            if bullet.x<1200 and bullet.x>0:
                bullet.x +=bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    keys=pygame.key.get_pressed()



    if keys[pygame.K_s]:
        bulletSound.play()
        if len(bullets)<2:
            if man.facing==1:
                facing=-1
            elif man.facing==0:
                facing =1
            #print(facing)
            bullets.append(projectile(man.x, man.y,facing))


    if keys[pygame.K_LEFT] and man.x>0:
        man.x -= man.vel
        man.left=True
        man.right=False
        man.standing=False
        man.facing=1
    if keys[pygame.K_RIGHT] and man.x<WIDTH-man.width-30:
        man.x += man.vel
        man.right=True
        man.left=False
        man.standing=False
        man.facing=0
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.y-=man.vel
            if man.y<0: man.y=0
        if keys[pygame.K_DOWN]:
            man.y+=man.vel
            #print(man.y)
            if man.y>620: man.y=620
        if keys[pygame.K_SPACE]:
            man.isJump=True

    else:
        if  man.jumpCount>=-10:
            neg=1
            if man.jumpCount<0:
                neg=-1
            man.y -= (man.jumpCount**2)*0.5*neg
            man.jumpCount-=1
        else:

            man.isJump=False
            man.jumpCount=10
   # print(man.x,man.y)


    draw()


pygame.quit()