import pygame
from maps import *

pygame.init()

win_w = 600
win_h = 500
FPS = 40


spring = pygame.transform.scale(pygame.image.load("background2.png"), (win_w, win_h))

block_size = 20




class GameSprite:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Pers(GameSprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed

    def move(self, key_left, key_right, key_up, key_down):
        k = pygame.key.get_pressed()
        if k[key_right]:
            if self.rect.right <= win_w:
                self.rect.x += self.speed 
        elif k[key_left]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed
        elif k[key_up]:
            if self.rect.y >= 0:
                self.rect.y -= self.speed
        elif k[key_down]:
            if self.rect.bottom <= win_h:
                self.rect.y += self.speed
        
class Button:
    def __init__(self, x, y, w, h, image1, image2):
        self.rect = pygame.Rect(x, y, w, h)
        self.image1 = pygame.transform.scale(image1, (w, h))
        self.image2 = pygame.transform.scale(image2, (w, h))
        self.image = self.image1

    def reset(self, x, y):
        self.animate(x, y)
        window.blit(self.image, (self.rect.x, self.rect.y))

    def animate(self, x, y):
        if self.rect.collidepoint(x, y):
            self.image = self.image2
        else:
            self.image = self.image1




class Enemy(GameSprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed



play_img = pygame.image.load("Play.png")
quit_img = pygame.image.load("Quit.png")






window = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Лaбиринт")
clock = pygame.time.Clock()
#window.fill((2, 200, 200))

btn_play = Button(win_w//2-100, (win_h-10)//5, 200, 50, play_img, play_img)
btn_quit = Button(win_w//2-100, (win_h-10)//5*3, 200, 50, quit_img, quit_img)

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (win_w, win_h))
window.blit(background, (0, 0))

pers_img = pygame.image.load("luntic.png")
pers = Pers(-6, 450, 45, 45, pers_img, 5)

gold_img = pygame.image.load("treasure.png")
gold = GameSprite(win_w - 60, win_h - 60, 50, 50, gold_img)

enemy_img = pygame.image.load("enemi_le.png")
enemy  = Enemy(50, 200, 35, 35, enemy_img, 0)
enemy_img2 = pygame.image.load("enemy_le2.png")
enemy2  = Enemy(200, 200, 35, 35, enemy_img2, 0)

enemys = [enemy, enemy2]

play_img = pygame.image.load("Play.png")
quit_img = pygame.image.load("Quit.png")

blocks = list()
block_img = pygame.image.load("block.png")
block_size = 40
x, y = 0, 0

for line in lvl:
    for s in line:
        if s == "1":
            block = GameSprite(x, y, block_size, block_size, block_img)
            blocks.append(block)
        x += 40
    x = 0
    y += 40

game = True

screen = "menu"

finish = False
while game:


    mouse_x, mouse_y = pygame.mouse.get_pos()

    if screen == "menu":
        window.blit(spring, (0, 0))
        btn_play.reset(mouse_x, mouse_y)
        btn_quit.reset(mouse_x, mouse_y)

    for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
               


    if not finish:
        window.blit(background, (0, 0))
        enemy.update()
        enemy2.update()
        pers.move(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        pers.update()
        gold.update()
        for block in blocks:
            block.update()
            if pers.rect.colliderect(block.rect):
                game = False
        for enemy in enemys:
            enemy.update()
            if pers.rect.colliderect(enemy.rect):
                game = False




        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False













            
    pygame.display.update()
    clock.tick(FPS)