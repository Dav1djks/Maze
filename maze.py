from pygame import *

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (65, 65)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y 
    
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x -=self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x +=self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y +=self.speed
class Enemy(GameSprite):
    direction='left'
    def update(self):
        if self.rect.x <= 470:
            self.direction="right"
        if self.rect.x >= win_width - 85:
            self.direction="left"
        
        if self.direction=='left':
            self.rect.x-=self.speed
        else:
            self.rect.x+=self.speed

class Wall(sprite.Sprite):
    def __init__(self, colour_1, colour_2, colour_3, wall_x, wall_y,wall_width,wall_height):
        super().__init__()
        self.colour_1=colour_1
        self.colour_2=colour_2
        self.colour_3=colour_3
        self.width=wall_width
        self.height=wall_height
        self.image=Surface((self.width,self.height))
        self.image.fill((colour_1,colour_2,colour_3))
        self.rect=self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



        

win_width=700
win_height=500
window=display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width,win_height))

player=Player("hero.png",5, win_height-80,4)
monster=Enemy('cyborg.png', win_width-200,280, 2)
final=GameSprite('treasure.png',  win_width-120  , win_height-80, 0)

w1=Wall(154,205,50,100,20,450,10)
w2=Wall(154,205,50,100,480,350,10)
w3=Wall(154,205,50,100,20,10,380)
w4=Wall(154,205,50,550,20,10,240)
w5=Wall(154,205,50,650,250,140,10)
w6=Wall(154,205,50,450,100,10,390)
w7=Wall(154,205,50,350,100,10,190)
w8=Wall(154,205,50,250,100,200,10)
w9=Wall(154,205,50,250,380,200,10)
w10=Wall(154,205,50,250,100,10,190)
w11=Wall(154,205,50,650,150,10,100)
w12=Wall(154,205,50,550,150,100,10)
w13=Wall(154,205,50,550,350,10,140)
w14=Wall(154,205,50,450,480,100,10)
w15=Wall(154,205,50,550,350,60,10)

game=True
finish=False
clock=time.Clock()
FPS=60

font.init()
font=font.SysFont('Arial',70)
win=font.render("You win!",True,(255,215,0))
lose=font.render("You lose!",True,(180,0,0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money=mixer.Sound('money.ogg')
kick=mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish !=True:
        window.blit(background,(0,0))
        player.update()
        monster.update()
        
        player.reset()
        monster.reset()
        final.reset()
        
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()

        if sprite.collide_rect(player,monster) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player,w7) or sprite.collide_rect(player,w8) or sprite.collide_rect(player,w9) or sprite.collide_rect(player,w10) or sprite.collide_rect(player,w11) or sprite.collide_rect(player,w12) or sprite.collide_rect(player,w13) or sprite.collide_rect(player,w14) or sprite.collide_rect(player,w15):
            finish=True
            window.blit(lose,(200,200))
            kick.play()

        if sprite.collide_rect(player,final):
            finish=True
            window.blit(win,(200,200))
            money.play


    display.update()
    clock.tick(FPS)

