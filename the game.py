import pygame as pg
import datetime
import time
pg.init()


WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Влево-выстрел-Вправо")

# zagruzka kartinok
nlo = pg.image.load("nlo.png")
enemy = pg.image.load("enemy.png")
bullet_pct = pg.image.load("bullet.png")
bg = pg.image.load("kosmos.png")
bullet = [-100,-100]
vy_bull = 0

# sozdanie teksta
font = pg.font.Font(None, 36)
text = font.render("You Win!!!", True, (0,255,0))
text_rect = text.get_rect(center=(200, 200))


# sozdanie playera
class Player():
    def __init__(self, px, py):
        self.px = px
        self.py = py

player = Player(100,500)
# sozdanie vragov
class Enemy():
    def __init__(self, ex, ey, vx):
        self.ex = ex
        self.ey = ey
        self.vx = vx
    def update(self):
        self.ex += self.vx
ex = 10
ey = 100
vx = 10
enemys = [Enemy(ex,ey,vx) for i in range(7)]
for i in range(7):
    enemys[i].ex += ex
    enemys[i].vx = 10
    ex += 100

# sozdanie pulek

class Bullet():
    def __init__(self, bx, by, vy):
        self.bx = bx
        self.by = by
        self.vy = vy
    def update(self):
        self.by -= self.vy
bullets = [Bullet(-100,-100,0)]



count = 0
nlo_rect = nlo.get_rect()
start_time = datetime.datetime.now()
# osnovnoi cikl
while True:
    
    
    for event in pg.event.get():
        if event.type == quit:
            pg.quit()

    # проверить кнопки
    # если кнопки нажаты, то изменить координаты игрока            
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        player.px += 10
    if keys[pg.K_LEFT]:
        player.px -= 10

    # ЕСЛИ нажат пробел И с момента создания предыдущей пульки прошло не менее 0.2 сек, ТО создать новую пульку
    if keys[pg.K_SPACE]:
        
        
        
        
        current_time = datetime.datetime.now()
        elapsed_time = current_time - start_time
        seconds = elapsed_time.total_seconds()

        if seconds >= 1:
            bullets.append(Bullet(player.px+5,player.py-100,0))
            bullets[-1].vy = 10
            start_time = datetime.datetime.now()
        
       

        
    
    #otrisovka osnovi
    screen.blit(bg, (0, 0))
    screen.blit(nlo, (player.px,player.py))
    for i in range(len(bullets)):
        screen.blit(bullet_pct,(bullets[i].bx,bullets[i].by))
        bullets[i].update()
    for i in range(len(enemys)):
        if len(enemys) == 0:
            text_scaled = pg.transform.scale(text,(600,200))
            screen.blit(text_scaled,text_rect)
        screen.blit(enemy,(enemys[i].ex, enemys[i].ey))
        enemys[i].update()
        if enemys[i].ex >= 800:
            
            enemys[i].vx = -10
        if enemys[i].ex <= 0:
            
            enemys[i].vx = 10
        
   
    for i in range(len(enemys)):
        
        # ubivanie
        for y in range(len(bullets)):
            
            if enemys[i].ex  < bullets[y].bx+50 < enemys[i].ex + 50 and enemys[i].ey  < bullets[y].by-50 < enemys[i].ey + 50:
                count += 1
                print("molodec")
                print(count)
                enemys[i].ey = 800
                enemys[i].ex = 900                  
                enemys[i].vx = 0
                
                bullets.pop()
                print(len(bullets))
            
    # proverka pobedi\
    
    if count == len(enemys):
        text_scaled = pg.transform.scale(text,(600,200))
        screen.blit(text_scaled,text_rect)
    
    pg.display.flip()
    time.sleep(1/120)

