import pygame,sys
from pygame.locals import *
pygame.init()
Screen = pygame.display.set_mode((600, 300))
Screen.fill((0xFF,0xFF,0xFF))
pygame.display.set_caption('My Game')

WHITE = pygame.Color(0xFF,0xFF,0xFF)
BLUE = pygame.Color(0, 0, 200)
RED = pygame.Color(200, 0, 0)
GREEN = pygame.Color(0, 200, 0)
man = []
for i in range(10):
    pic = pygame.image.load('run\\Run_00%d.png'%i)
    pic = pygame.transform.scale(pic, (200, 200))
    man += [pic]
backpic = pygame.image.load('back.png')
counter = 0
fpsClock = pygame.time.Clock()
pygame.key.set_repeat(1, 50)
Screen.blit(backpic, (0, 0))
Screen.blit(man[0], (0, 100))
deltax = 0
while True: # main game loop
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        keystate = pygame.key.get_pressed()
        
        if keystate[K_RIGHT]:
            Screen.blit(backpic, (600 - deltax, 0))
            Screen.blit(backpic, (-deltax, 0))
            Screen.blit(man[counter], (0, 100))
            counter = (counter + 1) % 9
            deltax = (deltax + 10) % 600
        #fpsClock.tick(10)
    pygame.display.update()
