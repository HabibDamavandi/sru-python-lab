import pygame, sys,time
from pygame.locals import *


center = (300,300)
def pos(sur):
    size = sur.get_size()
    hsize = [n / 2 for n in size]
    pos = (center[0] - hsize[0], center[1] - hsize[1])
    return pos


pygame.init()
Screen = pygame.display.set_mode((600, 600))
Screen.fill((0xFF, 0xFF, 0xFF))
pygame.display.set_caption('CLOCK')

backpic = pygame.image.load('clock.png').convert_alpha()
hour = pygame.image.load('hourhand.png')
minute = pygame.image.load('minutehand.png')
second = pygame.image.load('secondhand.png')

fpsClock = pygame.time.Clock()
Screen.blit(backpic, (0, 0))
ang = -6
while True:  

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    now = time.localtime(time.time())
    sec = pygame.transform.rotate(second,ang*now.tm_sec)
    min = pygame.transform.rotate(minute,ang*now.tm_min)
    hur = pygame.transform.rotate(hour,(ang*5*now.tm_hour)-(now.tm_min/2))
    Screen.blit(backpic,(0,0))
    Screen.blit(min,pos(min))
    Screen.blit(hur,pos(hur))
    Screen.blit(sec, pos(sec))
    fpsClock.tick(10)

    pygame.display.update()
