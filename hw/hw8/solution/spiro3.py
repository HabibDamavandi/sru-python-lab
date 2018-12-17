"""
Create Spirograph curves made by one circle of radius r2 rolling 
around the inside (or outside) of another of radius r1.  The pen
is a distance r3 from the center of the first circle.
"""
import pygame,sys
from pygame.locals import *
import datetime
from math import *

pygame.init()
wx = 600
wy = 600
screen = pygame.display.set_mode((wx, wy), 0, 32)
background = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
foreground = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
background.fill((0xFF,0xFF,0xFF))
pygame.display.set_caption('Spirograph')

WHITE = pygame.Color(0xFF,0xFF,0xFF)
RED = pygame.Color(0xFF,0x00,0x00)
GREEN = pygame.Color(0x00,0xFF,0x00)
BLUE = pygame.Color(0x00,0x00,0xFF)
TGREEN = pygame.Color(0x00,0xFF,0x00,0xAA)

fpsClock = pygame.time.Clock()
r1 = 290
r2 = 170
r3 = 140
prevPoint = (r1-r2+r3+wx/2, 0+wy/2)
alfa1 = 0.0
alfa2 = 0.0
ncycle = r2/gcd(r1,r2)
while True: # main game loop
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    fpsClock.tick(20)

    if(alfa1 < ncycle*2*pi):
        cx = (r1-r2)*cos(alfa1) + wx/2
        cy = (r1-r2)*sin(alfa1) + wy/2
        x = cx + r3*cos(alfa2)
        y = cy + r3*sin(alfa2)

        pygame.draw.line(background,RED,prevPoint,(x, y),1)
        screen.blit(background, (0, 0))
        
        foreground.fill((0xFF,0xFF,0xFF,0x00))
        pygame.draw.circle(foreground,BLUE,(int(wx/2), int(wy/2)),r1, 5)
        pygame.draw.circle(foreground,TGREEN,(int(cx),int(cy)),r2)
        pygame.draw.circle(foreground,RED,(int(x),int(y)),5)
        screen.blit(foreground, (0, 0))
        
        prevPoint = (x, y)
        alfa1 += 0.1
        alfa2 = (-(r1/r2)*alfa1)
        
        pygame.display.update()

