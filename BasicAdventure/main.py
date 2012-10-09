import pygame
from pygame.locals import *

D = pygame.display.set_mode((640,480))
from data import *
from math import *
baseTileset = Tileset("files/tileset.png",32,(10,8))
lightGreyFloor = LightGreyFloor((5,0),baseTileset)
levelrepr1 = [[lightGreyFloor,lightGreyFloor,lightGreyFloor,lightGreyFloor,lightGreyFloor],
[lightGreyFloor,lightGreyFloor,lightGreyFloor,lightGreyFloor,lightGreyFloor],
[lightGreyFloor,lightGreyFloor,lightGreyFloor,lightGreyFloor,lightGreyFloor],
[lightGreyFloor,lightGreyFloor,lightGreyFloor,lightGreyFloor,lightGreyFloor],
[lightGreyFloor,lightGreyFloor,lightGreyFloor,lightGreyFloor,lightGreyFloor]]

level1 = Level("level1",(5,5))
level1.setLevel(levelrepr1)

while 1:
    level1.blitLevel(D)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    pygame.display.flip()