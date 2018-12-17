import pygame,sys
from pygame.locals import *
import datetime
from math import *
import numpy as np

WX = 1000
WY = 400

WHITE = pygame.Color(0xFF,0xFF,0xFF)
RED = pygame.Color(0xFF,0x00,0x00)
GREEN = pygame.Color(0x00,0xFF,0x00)
BLUE = pygame.Color(0x00,0x00,0xFF)

hbed = WY/30
wbed = 6*WX/8
xbed = (WX-wbed)/2
ybed = 7*WY/8
wcylinder = WX/60
xcylinder = xbed+wbed/6-wcylinder/2
ycylinder = WY/3
hcylinder = ybed-ycylinder
topy = WY/4
gapcylinder = wbed/3
wdisk = gapcylinder
hdisk = 1.5*hbed
bedRect = pygame.Rect(xbed, ybed, wbed, hbed)
cylRectA = pygame.Rect(xcylinder, ycylinder, wcylinder, hcylinder)
cylRectB = pygame.Rect(xcylinder+gapcylinder, ycylinder, wcylinder, hcylinder)
cylRectC = pygame.Rect(xcylinder+2*gapcylinder, ycylinder, wcylinder, hcylinder)

class Hanoi():  
    def __init__(self, n):
        self.n = n
        self.solution=[]
        self.getSolution(n,0,1,2)
        self.counter = 0
        self.busy = False        
        self.cylinders = [Cylinder(cylRectA),Cylinder(cylRectB),Cylinder(cylRectC)]
        for i in range(1,n+1):
            diskColor = pygame.Color(0x00,int(0x55+i/n*0x88),0x00,0xAA)
            diskRect = pygame.Rect(xbed+wbed/6-(wdisk-25*i)/2, ybed-i*(hdisk+2), wdisk-25*i, hdisk)
            self.cylinders[0].addDisk(Disk(diskColor,diskRect))
    
    def getSolution(self,n,a,b,c):
        if n == 1:
            self.solution += [(a,c)]
        else:
            self.getSolution(n-1,a,c,b)
            self.getSolution(1,a,b,c)
            self.getSolution(n-1,b,a,c)
            
    def move(self):
        if self.busy:
            self.busy = self.currentDisk.ismoving
        elif(self.counter < len(self.solution)):
            source = self.solution[self.counter][0]
            dest = self.solution[self.counter][1]        
            
            disk = self.cylinders[source].removeDisk()
            self.currentDisk = disk
            self.cylinders[dest].addDisk(disk)
            x = self.cylinders[dest].getCenter()[0] - disk.rect.width/2
            y = self.cylinders[dest].getTop()        
            disk.startMoveToxy(x,y)            
            self.busy = disk.ismoving
            self.counter += 1


class Cylinder(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer      
        self.image = pygame.Surface(rect.size)
        self.image.fill(RED)
        self.rect = rect
        self.disks = []
        
    def addDisk(self,disk):
        self.disks += [disk]
    
    def removeDisk(self):
        disk = self.disks[-1]
        del self.disks[-1]
        return disk
    
    def getTop(self):
        n = len(self.disks)
        return ybed - n * (hdisk + 2)
        
    def getCenter(self):
        return self.rect.center
        
class Disk(pygame.sprite.Sprite):
    def __init__(self, color, rect):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer        
        self.image = pygame.Surface(rect.size)
        self.image.fill(color)
        self.rect = rect
        self.ismoving = False
        self.progress = 0

    def startMoveToxy(self,x1,y1):
        self.ismoving = True
        x0 = self.rect.left
        y0 = self.rect.top
        self.xpath = np.hstack((np.ones(33)*x0, np.linspace(x0,x1,34),np.ones(33)*x1))
        self.ypath = np.hstack((np.linspace(y0,topy,33),np.ones(34)*topy, np.linspace(topy,y1,33)))
        self.progress = 0
        
    def moveDisk(self):
        #move the disk to the destination cylinder
        self.progress += 1
        if self.progress == 100:
            self.ismoving = False
        else:
            self.rect.topleft = self.xpath[self.progress],self.ypath[self.progress]

    def update(self):
        if self.ismoving:
            self.moveDisk()

    
def main():
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((WX, WY), 0, 32)
    screen.fill((0xFF,0xFF,0xFF))
    pygame.display.set_caption('Hanoi')

    fpsClock = pygame.time.Clock()

    theHanoi = Hanoi(4)
    
    allsprites = pygame.sprite.RenderPlain((theHanoi.cylinders,theHanoi.cylinders[0].disks))

    while True: # main game loop
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        allsprites.update()
        
        #Draw Everything
        screen.fill((0xFF,0xFF,0xFF))
        pygame.draw.rect(screen,BLUE,bedRect)
        theHanoi.move()
        allsprites.draw(screen)
        
        fpsClock.tick(100)            
        pygame.display.update()
        
#this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()

