import pygame
import time
import sys
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

# Draws game box
screenwidth = 800
screenheight = 500
win = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption('Chaos Horde | MDF')

#Set up player sprites and backgrounds
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load(
                 'R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load(
                'L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')
bkg = pygame.image.load('bg5.jpg')
bkg2 = pygame.image.load('MDF Logo.png')
bkg3 = pygame.image.load('bg4.jpg')
platform2 = pygame.image.load('platform.jpg')

#Background Music
music = pygame.mixer.music.load("Hero.mp3")
pygame.mixer.music.play(-1)
effect = pygame.mixer.Sound('laser2.wav')
effect.set_volume(0.2)
clock = pygame.time.Clock()


score = 0
black = (0, 0, 0)
WHITE = (255, 255, 255)
TITLE = "Chaos Horde"
Highestwave = 0

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.powervel = 10
        self.isjump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.wave = 0
        self.hitbox = (self.x + 17, self.y + 11, 29, 59)
        self.health = 5

# Function
    def draw(self, win):

        if (self.walkcount + 1) >= 27:
            self.walkcount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkcount//3], (self.x, self.y))
                self.walkcount += 1
                pygame.display.update()

            elif self.right:
                win.blit(walkRight[self.walkcount//3], (self.x, self.y))
                self.walkcount += 1
                pygame.display.update()

        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 59)
        #pygame.draw.rect(win, (255,0, 0), self.hitbox,2)

    def hit(self):
        self.isjump = False
        self.jumpCount = 10
        self.x = 400
        self.y = 90
        self.WalkCount = 0
        reload = True
        bulletamount = 10
        powervelboolean = False
        self.health -= 1
        font1 = pygame.font.SysFont('arial', 100)
        text = font1.render("-" + str(self.wave),1, (255, 0, 0))
        win.blit(text, (screenwidth/2 -(text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(1)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.QUIT()

    def bosshit(self):
        self.isjump = False
        self.jumpCount = 10
        self.x = 400
        self.y = 90
        self.WalkCount = 0
        reload = True
        bulletamount = 10
        powervelboolean = False
        self.health -= 2
        font1 = pygame.font.SysFont('arial', 100)
        text = font1.render("-" + str(self.wave * 2),1, (255, 0, 0))
        win.blit(text, (screenwidth/2 -(text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(1)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.QUIT()

    def winner(self):
            font1 = pygame.font.SysFont('arial', 25, True)
            text1 = font1.render('Press Enter to exit',1, (0, 0, 0))
            win.blit(text1, (150, 300))
            pygame.display.update()

    def show_start_screen(self):
    # game splash/start screen
        win.blit(bkg, (0, 0))
        self.draw_text(TITLE, 48, black, screenwidth / 2, screenheight / 4)
        self.draw_text("Arrows to move, Space to jump", 22, black, screenwidth / 2, 300)
        self.draw_text("Press p to shoot", 22, black, screenwidth / 2, 330)
        self.draw_text("Press a key to play", 22, black, screenwidth / 2, 360)
        self.draw_text("Press r to reload", 22, black, screenwidth / 2, 390)
        self.draw_text("Press s to dash", 22, black, screenwidth / 2, 420)
        self.draw_text("MDF | Ameen", 48, black, 100, 450)
        self.draw_text("Discord: discord.gg/G7r3U72", 48, black, 600, 450)
        self.draw_text("Highest Wave: " + str(Highestwave), 48, black, 300, 450)
        pygame.display.flip()
        self.wait_for_key()


    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('arial', 30)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        win.blit(text_surface, text_rect)

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
    def delay(self):
        i = 0
        i = 0
        while i < 300:
            pygame.time.delay(5)
            i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 301
                pygame.QUIT()
        
    def loading(self):
        win.blit(bkg2, (150, 0))
        pygame.display.flip()
        self.delay()

    def wavenum(self):
        self.wave += 1
        font2 = pygame.font.SysFont('arial', 100)
        text = font2.render('Wave ' + str(self.wave),1, (255, 0, 0))
        win.blit(text, (screenwidth/2 -(text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        i = 0
        while i < 300:
            pygame.time.delay(1)
            i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 301
                pygame.QUIT()
        
    
class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = WHITE
        #self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class enemy(object):
    walkRight = [pygame.image.load(f'R{i}B.png') for i in range(1,12)]
    walkLeft = [pygame.image.load(f'L{i}B.png') for i in range(1,12)]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end 
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = enemyvel
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.bosshealth = 100
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount +=1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount +=1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) 
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            #50 - (5* (10 -self.health)) is the same as 5 * self.health
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox ,2)
            
    def bossdraw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount +=1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount +=1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 100, 10)) 
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, self.bosshealth, 10))
            #50 - (5* (10 -self.health)) is the same as 5 * self.health
            self.hitbox = (self.x, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox ,2)


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x +=self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
    def bosshit(self):
        if self.bosshealth > 1:
            self.bosshealth -= 1
        else:
            self.visible = False
        
class boss(object):
    walkRight = [pygame.image.load(f'R{i}B.png') for i in range(1,12)]
    walkLeft = [pygame.image.load(f'L{i}B.png') for i in range(1,12)]

    def __init__(self, x, y, width, height, end):
        self.x =x
        self.y= y
        self.width = width
        self.height = height
        self.end = end 
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 15
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.bosshealth = 100
        self.visible = True

    def bossdraw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount +=1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount +=1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 100, 10)) 
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, self.bosshealth, 10))
            #50 - (5* (10 -self.health)) is the same as 5 * self.health
            self.hitbox = (self.x, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox ,2)


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x +=self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
                
    def bosshit(self):
        if self.bosshealth > 1:
            self.bosshealth -= 1
        else:
            self.visible = False

def redrawGameWindow():
    font3 = pygame.font.SysFont('arial', 10)
    win.blit(bkg3, (0, 0))
    text = font.render('Score: ' + str(score), 1, (WHITE))
    win.blit(text, (100, 465))
    win.blit(platform2, (300, 150))
    text1 = font.render('[Press Enter to exit]',1, (0, 0, 0))
    win.blit(text1, (50, 10))
    #text2 = font.render('Ammo: ' + str(bulletamount),1, (0, 0, 0))
    #win.blit(text2, (460, 10))
    text3 = font.render('Wave: ' + str(man.wave), 1, (WHITE))
    win.blit(text3, (350, 465))
    #text4 = font.render('HP: ' + str(man.health), 1, (WHITE))
    #win.blit(text4, (250, 465))
    #Displaying Time
    if minute < 10 and sec > 9 and minute < 100:
        text5 = font.render('Time: 0' + str(minute) + ':' + str(sec), 1, (WHITE))
        win.blit(text5, (600, 465))
    if minute < 10 and sec < 10 and minute < 100:
        text5 = font.render('Time: 0' + str(minute) + ':0' + str(sec), 1, (WHITE))
        win.blit(text5, (600, 465))
    if minute > 9 and sec > 10 and minute < 100: 
        text5 = font.render('Time: ' + str(minute) + ':' + str(sec), 1, (WHITE))
        win.blit(text5, (600, 465))
    if minute > 9 and sec < 10 and minute < 100:
        text5 = font.render('Time: ' + str(minute) + ':0' + str(sec), 1, (WHITE))
        win.blit(text5, (600, 465))
    if minute > 99:
        text5 = font.render('Time: 99:59+', 1, (WHITE))
        win.blit(text5, (600, 465))
    man.draw(win)
    goblin.draw(win)
    #Display HP
    width3 = 10
    healthx = 500
    healthy = 25
    pygame.draw.rect(win, (255,0,0), (healthx, healthy, 25 * width3 , width3)) 
    pygame.draw.rect(win, (0,128,0), (healthx, healthy, 5 * man.health * width3, width3))
    #Display Bullets
    if bulletamount == 10:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 40,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 60,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 80,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 100,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 120,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 140 ,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 160,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 180,15,15))
    elif bulletamount == 9:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 40,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 60,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 80,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 100,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 120,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 140 ,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 160,15,15))
    elif bulletamount == 8:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 40,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 60,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 80,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 100,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 120,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 140 ,15,15))
    elif bulletamount == 7:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 40,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 60,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 80,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 100,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 120,15,15))
    elif bulletamount == 6:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 40,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 60,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 80,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 100,15,15))
    elif bulletamount == 5:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 40,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 60,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 80,15,15))
    elif bulletamount == 4:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 40,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 60,15,15))
    elif bulletamount == 3:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 40,15,15))
    elif bulletamount == 2:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
    elif bulletamount == 1:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
    elif bulletamount > 10 and bulletamount <100:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 40,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 60,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 80,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 100,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 120,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 140 ,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 160,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 180,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 200,15,15))
        bulletamount2 = bulletamount - 10
        text6 = font3.render('+' + str(bulletamount2),1, (0, 0, 0))
        win.blit(text6, (750, bullettop + 200))
    elif bulletamount >99:
        pygame.draw.rect(win, (255,128,0), (750,bullettop,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 20,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 40,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 60,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 80,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 100,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 120,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 140 ,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 160,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 180,15,15))
        pygame.draw.rect(win, (255,128,0), (750,bullettop + 200,15,15))
        bulletamount2 = bulletamount - 10
        text7 = font3.render(str(bulletamount2) + '+',1, (0, 0, 0))
        win.blit(text7, (750, bullettop + 200))
    for bullet in bullets:
        bullet.draw(win)
    goblin2.draw(win)
    goblin3.draw(win)
    goblinboss.bossdraw(win)
    pygame.display.update()
def GameOver():
    font2 = pygame.font.SysFont('arial', 100)
    text = font2.render('Game Over',1, (255, 0, 0))
    win.blit(text, (250, screenheight/2))
    pygame.display.update()
    i = 0
    i = 0
    while i < 300:
        pygame.time.delay(3)
        i += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            i = 301
            pygame.QUIT()

#varible setting
dash = True
Highestwave = 0
dashcooldown = 0
platform = 400
bullettop = 50
enemyspeedexchange = True
font = pygame.font.SysFont('arial', 30, True)
enemyvel = 5
man = player(300, platform, 64, 64)
bulletamount = 10
goblin = enemy(20, platform, 64, 64,450)
goblin2 = enemy(400, 415, 64, 64, 720)
goblin3 = enemy(200, 413, 64, 64, 500) #The first value is the starting x value of the enemy and last value is the end x value of the enemy
goblinboss = boss(20, 410, 64, 64, 760)
goblin2.visible = False
goblin.visible = False
goblin3.visible = False
goblinboss.visible = False
powervelboolean = False
instantreload = False
bulletcooldown = 3
shootLoop = 0
bullets = []
reload = True
fly = False
man.loading()
man.show_start_screen()
counter = 0
dashtime = 0
dashing = False
dashingstoptime = 0
time = 0
sec = 0
minute = 0
run = True
#main loop
while run:
    #Time
    clock.tick(27)
    time += 1
    dashtime +=1
    if time == 27:
        time = 0
        sec += 1
    if sec == 60:
        sec = 0
        minute += 1
    if dashtime == 27:
        dashtime = 0
        if dash == False:
            dashcooldown +=1
        if dashing == True:
            dashingstoptime +=1
    if dashingstoptime == 1:
        dashing = False
        dashingstoptime = 0
    if dashcooldown == 4:
        dashcooldown = 0
        dash = True

    #What happens when the player gets hit
    if goblin.visible == True and dashing == False:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0]< goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                enemyvel += counter
                goblin.vel = enemyvel
                goblin2.vel = enemyvel
                goblin3.vel = enemyvel
                counter = 0
                reload = True
                fly = False
                bulletamount = 10
                powervelboolean = False
                instantreload = False
                score -= man.wave
    if goblin2.visible == True and dashing == False:
        if man.hitbox[1] < goblin2.hitbox[1] + goblin2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin2.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin2.hitbox[0] and man.hitbox[0]< goblin2.hitbox[0] + goblin2.hitbox[2]:
                man.hit()
                enemyvel +=counter
                goblin.vel = enemyvel
                goblin2.vel = enemyvel
                goblin3.vel = enemyvel
                counter = 0
                reload = True
                fly = False
                bulletamount = 10
                powervelboolean = False
                instantreload = False
                score -= man.wave
    if goblin3.visible == True and dashing == False:
        if man.hitbox[1] < goblin3.hitbox[1] + goblin3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin3.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin3.hitbox[0] and man.hitbox[0]< goblin3.hitbox[0] + goblin3.hitbox[2]:
                man.hit()
                enemyvel += counter
                goblin.vel = enemyvel
                goblin2.vel = enemyvel
                goblin3.vel = enemyvel
                counter = 0
                reload = True
                fly = False
                bulletamount = 10
                powervelboolean = False
                instantreload = False
                score -= man.wave
    if goblinboss.visible == True and dashing == False:
        if man.hitbox[1] < goblinboss.hitbox[1] + goblinboss.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblinboss.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblinboss.hitbox[0] and man.hitbox[0]< goblinboss.hitbox[0] + goblinboss.hitbox[2]:
                man.bosshit()
                enemyvel += counter
                goblin.vel = enemyvel
                goblin2.vel = enemyvel
                goblin3.vel = enemyvel
                counter = 0
                reload = True
                fly = False
                bulletamount = 10
                powervelboolean = False
                instandreload = False
                score -= (man.wave * 2)


    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    #What happens when a goblin is hit 
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                if goblin.visible:
                    goblin.hit()
                    bullets.pop(bullets.index(bullet))
                    score += 1
        if bullet.x < screenwidth and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin2.hitbox[1] + goblin2.hitbox[3] and bullet.y + bullet.radius > goblin2.hitbox[1]:
            if bullet.x + bullet.radius > goblin2.hitbox[0] and bullet.x - bullet.radius < goblin2.hitbox[0] + goblin2.hitbox[2]:
                if goblin2.visible:
                    goblin2.hit()
                    bullets.pop(bullets.index(bullet))
                    score += 1

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin3.hitbox[1] + goblin3.hitbox[3] and bullet.y + bullet.radius > goblin3.hitbox[1]:
            if bullet.x + bullet.radius > goblin3.hitbox[0] and bullet.x - bullet.radius < goblin3.hitbox[0] + goblin3.hitbox[2]:
                if goblin3.visible:
                    goblin3.hit()
                    bullets.pop(bullets.index(bullet))
                    score += 1

    for bullet in bullets:
        if bullet.y - bullet.radius < goblinboss.hitbox[1] + goblinboss.hitbox[3] and bullet.y + bullet.radius > goblinboss.hitbox[1]:
            if bullet.x + bullet.radius > goblinboss.hitbox[0] and bullet.x - bullet.radius < goblinboss.hitbox[0] + goblinboss.hitbox[2]:
                if goblinboss.visible:
                    goblinboss.bosshit()
                    bullets.pop(bullets.index(bullet))
                    score += 1
    #Normal Keys
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_p] and shootLoop == 0 and reload == True:
        effect.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < bulletcooldown : #Adjust the amount of bullets on the screen at one time
            bulletamount -=1
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0, 0, 0), facing ))
        if bulletamount == 0:
            reload = False
        shootLoop = 1
    if keys[pygame.K_r] and bulletamount < 10 and instantreload == False:
        reload = True
        pygame.time.delay(10)
        bulletamount += 1
    if keys[pygame.K_r] and bulletamount < 10 and instantreload == True:
        reload = True
        bulletamount = 10
    if keys[pygame.K_m] and score > 49 and bulletamount <11:
        bulletamount = 60
        reload = True
        score -=50
    if keys[pygame.K_o] and score >= 200 and powervelboolean == False:
        score -=200
        powervelboolean = True
    if keys[pygame.K_i] and score >= 200 and instantreload == False:
        score -=200
        instantreload = True
    if keys[pygame.K_u] and score >=50 and bulletcooldown < 10:
        bulletcooldown +=1
        score -=50
    if keys[pygame.K_e] and score >=50 and enemyvel > 1:
        score -=50
        enemyvel -=1
        goblin.vel = enemyvel
        goblin2.vel = enemyvel
        goblin3.vel = enemyvel
        counter +=1
    if keys[pygame.K_f] and score >=1000 and fly == False:
        score -=1000
        fly = True
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and fly == True and man.y > man.vel:
        man.y -= man.vel
    if (keys[pygame.K_DOWN] or keys[pygame.K_x]) and man.y < screenheight - man.height - man.vel and fly == True:
        man.y += man.vel
    if keys[pygame.K_h] and score >=50 and man.health < 3:
        man.health += 1
        score -=50
    if keys[pygame.K_t] and enemyspeedexchange == True:
        enemyvel += 1
        goblin.vel = enemyvel
        goblin2.vel = enemyvel
        goblin3.vel = enemyvel
        score +=30
        enemyspeedexchange = False

        
        
        
    #Movement
    if powervelboolean == False:
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and man.x < screenwidth - man.width - man.vel:
            man.x += man.vel
            man.left = False
            man.right = True
            man.standing = False
        else:
            man.standing = True
            man.walkcount = 0
    if powervelboolean == True:
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and man.x > man.powervel:
            man.x -= man.powervel
            man.left = True
            man.right = False
            man.standing = False
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and man.x < screenwidth - man.width - man.vel:
            man.x += man.powervel
            man.left = False
            man.right = True
            man.standing = False
        else:
            man.standing = True
            man.walkcount = 0
    if man.right == True and dash == True and keys[pygame.K_s]:
        dashing = True
        man.x +=50
        dash = False
    if man.left == True and dash == True and keys[pygame.K_s]:
        dashing = True
        man.x -=50
        dash = False
    if man.x > 780:
        man.x = 0
    if man.x < 0:
        man.x = 735
    
        
    #Jumping
    if not(man.isjump):
        if keys[pygame.K_SPACE] and man.y == platform:
            man.isjump = True
            man.walkcount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount <= 0:
                neg = -1    
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
            # time.sleep(0.04) - Use this to add an delay to jump
        else:
            man.isjump = False
            man.jumpCount = 10
            man.vel = 5
            

    #Goblin Respawn
    if goblin.visible == False and goblin2.visible == False and goblin3.visible == False and goblinboss.visible == False and man.wave < 5:
        man.wavenum()
        enemyspeedexchange = True
        goblin = enemy(40, platform, 64, 64,450)
        goblin2 = enemy(400, platform, 64, 64, 760)
    if goblin.visible == False and goblin2.visible == False and goblin3.visible == False and goblinboss.visible == False and man.wave > 4 and man.wave < 15:
        man.wavenum()
        enemyspeedexchange = True
        goblin = enemy(40, platform, 64, 64,450)
        goblin2 = enemy(400, platform, 64, 64, 760)
        goblin3 = enemy(200, 413, 64, 64, 500)
    #if goblin.visible == False and goblin2.visible == False and goblin3.visible == False and score < 50 and goblinboss.visible == False and man.wave >= 10:
        #enemyvel += 1
        #man.wavenum()
        #enemyspeedexchange = True
        #goblin = enemy(40, platform, 64, 64,450)
        #goblin2 = enemy(400, platform, 64, 64, 760)
        #goblin3 = enemy(200, platform, 64, 64, 500)
    if goblin.visible == False and goblin2.visible == False and goblin3.visible == False and goblinboss.visible == False and man.wave >= 14:
        enemyvel += 1
        man.wavenum()
        enemyspeedexchange = True
        goblin = enemy(20, platform, 64, 64,450)
        goblin2 = enemy(400, platform, 64, 64, 760)
        goblin3 = enemy(200, platform, 64, 64, 500)
        goblinboss = enemy(20, platform, 64, 64, 760)

    #Top Platform
    if man.y == 90 and man.x > 260 and man.x < 490:
            man.y -= 25
            
    #Other Stuff
    if keys[pygame.K_RETURN]:
        break
        pygame.quit()
    if man.y < platform and man.isjump == False and fly == False:
        man.y += 25
    if man.y > platform and man.isjump == False and fly == False:
        man.y = platform
    
    #What happens if you die
    if man.health == 0:
        GameOver()
        Highestwave = man.wave
        goblin.visible = False
        goblin2.visible = False
        goblin3.visible = False
        goblinboss.visible = False
        man.health = 5
        man.wave = 0
        man.x = 300
        man.y = platform
        score = 0
        enemyvel = 5
        goblin.vel = enemyvel
        goblin2.vel = enemyvel
        goblin3.vel = enemyvel
        counter = 0
        time = 0
        sec = 0
        minute = 0
        powervelboolean = False
        instantreload = False
        bulletcooldown = 3
        shootLoop = 0
        bullets = []
        reload = True
        fly = False
        bulletamount = 10
        enemyspeedexchange = True
        dash = True
        dashcooldown = 0
        dashtime = 0
        dashing = False
        dashingstoptime = 0
        man.show_start_screen()
        
        
    redrawGameWindow()
    #Used for Music
    pygame.event.poll()

    #Red Cross to close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
pygame.quit()
