import pygame,sys
from pygame.locals import *
import datetime
import math

pygame.init()
Screen = pygame.display.set_mode((600, 600))
Screen.fill((0xFF,0xFF,0xFF))
pygame.display.set_caption('My Game')

GRAYh = pygame.Color(0x20,0x20,0x20)
GRAYm = pygame.Color(0x50,0x50,0x50)
RED = pygame.Color(0xFF,0x00,0x00)

backpic = pygame.image.load('1.png')
backpic = pygame.transform.scale(backpic, (600, 600))

fpsClock = pygame.time.Clock()
Screen.blit(backpic, (0, 0))
rs = 230
rm = 180
rh = 150
while True: # main game loop
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    Screen.fill((0xFF,0xFF,0xFF))
    Screen.blit(backpic,(0, 0))
    time = datetime.datetime.now()
    alfas = -((time.second+time.microsecond/1000000) * (2*math.pi)/60)+ math.pi/2
    alfam = -(time.minute * (2*math.pi)/60)+ math.pi/2
    alfah = -((time.hour + time.minute/60) * (2*math.pi)/12)+ math.pi/2
    
    pygame.draw.line(Screen,GRAYh,(300,300),(300+rh * math.cos(alfah), 300-rh * math.sin(alfah)),12)
    pygame.draw.line(Screen,GRAYm,(300,300),(300+rm * math.cos(alfam), 300-rm * math.sin(alfam)),8)
    pygame.draw.line(Screen,RED,(300,300),(300+rs * math.cos(alfas), 300-rs * math.sin(alfas)),2)

    fpsClock.tick(30)
    pygame.display.update()
