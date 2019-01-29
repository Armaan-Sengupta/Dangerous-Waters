import pygame
import random
import os

black = (0,0,0)
white = (255,255,255)

length=1025
hight=768
size = [length,hight]
pygame.init()
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption("Dangerous Waters")
carryon = True
clock = pygame.time.Clock()

game_folder=os.path.dirname(__file__)
image_folder=os.path.join(game_folder,"Images")
background1=pygame.image.load(os.path.join(image_folder,"bg1.png"))
background2=pygame.image.load(os.path.join(image_folder,"bg2.png"))

#setting font
font = pygame.font.Font(None, 30)

#music setup

pygame.mixer.init()
pygame.mixer.music.load("Upside_Down.mp3")
pygame.mixer.music.play(-1)



#setting score
score=0
time=0
bg1=0
bg2=length

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #load and scale image
        self.image=pygame.transform.flip(pygame.image.load(os.path.join(image_folder,"fish11.png")).convert_alpha(), True, False)
        #self.image=pygame.transform.scale(self.image,[100,100])
        
        #if  you want surfaace
        #self.image = pygame.Surface([50,50])
        #self.image.fill(black)
        
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = hight/2
        self.time=0
    def update(self):
        pressed=pygame.key.get_pressed()
        """
        if pressed[pygame.K_UP]:
            self.rect.y-=5
        elif pressed[pygame.K_DOWN]:
            self.rect.y+=5
        """
        if pressed[pygame.K_SPACE]: #and self.time-4<time:
            self.rect.y-=10
            self.time=time+8
        elif self.time+5<time:
            self.rect.y+=5
        if self.rect.y<=0:
            self.rect.y+=10
        elif self.rect.y>hight-140:
            self.rect.y-=6
        

class Creator(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pair_count=0
        self.image = pygame.Surface([0,0])
        self.image.fill(black)
        self.rect = self.image.get_rect()
    def update(self):
        if self.pair_count<1:
            creator.create()
            self.pair_count+=1
    def create(self):
        self.free_gap=random.randint(100,120)
        self.anchor_hight=random.randint(100,600)
        self.rock_hight=hight-(self.anchor_hight+self.free_gap)
        anchor=Anchor(self.anchor_hight)
        rock=Rock(self.rock_hight)
        all_sprites.add(anchor)
        all_sprites.add(rock)
class Anchor(pygame.sprite.Sprite):
    def __init__(self,phight):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join(image_folder,"Anchor.png"))
        self.rect=self.image.get_rect()
        self.rect.x=length
        self.rect.y=phight-600
    def update(self):
        self.rect.x-=5
        if self.rect.x<=0:
            creator.pair_count-=1
            Increase_Score(1)
            self.kill()
        if self.rect.colliderect(player):
            EndGame()
class Rock(pygame.sprite.Sprite):
    def __init__(self,phight):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join(image_folder,"Volcano.png"))
        self.rect=self.image.get_rect()
        self.rect.x=length
        self.rect.y=hight-phight
    def update(self):
        try:
            self.rect.x=anchor.rect.x
        except:
            self.rect.x-=5
        if self.rect.x<=0:
            self.kill()
        if self.rect.colliderect(player):
            EndGame()

def Increase_Score(amount):
    global score
    score+=amount
def EndGame():
    global carryon
    carryon=False



all_sprites = pygame.sprite.Group() # sprite group
player=Player() # creating player object
all_sprites.add(player) #adding player object to sprite group
creator=Creator()
all_sprites.add(creator)
temp_count=1
while temp_count<3:
    background3=pygame.image.load(os.path.join(image_folder,"intro_bg"+str(temp_count)+".png"))
    screen.blit(background3,[bg1,0])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                temp_count+=1

while carryon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryon = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                pass

    
    screen.fill(white)
    bg1-=5
    bg2-=5
    
    if bg1==0:
        bg2=length
    elif bg2==0:
        bg1=length
    screen.blit(background1,[bg1,0])
    screen.blit(background2,[bg2,0])

    #Keyboard handling
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        carryon=False

    
    #displaying font on the screen
    text = font.render("Score: "+str(score), True, white)
    screen.blit(text, [925,10])

    
    all_sprites.update()
    all_sprites.draw(screen)
    clock.tick(60)
    pygame.display.flip()
    time+=1
temp_count=0
while temp_count<1:
    background4=pygame.image.load(os.path.join(image_folder,"Gameover.png"))
    screen.blit(background4,[0,0])
    font = pygame.font.Font(None, 80)
    text = font.render("Final Score: "+str(score), True, white)
    screen.blit(text, [length/2,600])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE or event.key==pygame.K_ESCAPE:
                temp_count+=1
pygame.quit()
print(score)












        
