import pygame
from pygame.locals import *

D = pygame.display.set_mode((640,480))
from data import *
from math import *
baseTileset = Tileset("files/tileset.png",32,(10,8))
lightGreyFloor = LightGreyFloor(baseTileset)
lightGreyFloor2 = LightGreyFloor2(baseTileset)
straightUpRoad=StraightUpRoad(baseTileset)
staightSideRoad=StaightSideRoad(baseTileset)
turnUpLeftRoad=TurnUpLeftRoad(baseTileset)
turnUpRightRoad=TurnUpRightRoad(baseTileset)
turnDownLeftRoad=TurnDownLeftRoad(baseTileset)
turnDownRightRoad=TurnDownRightRoad(baseTileset)

levelrepr1 = [[turnUpLeftRoad,staightSideRoad,staightSideRoad,staightSideRoad,turnUpRightRoad],
[straightUpRoad,lightGreyFloor2,lightGreyFloor,lightGreyFloor2,straightUpRoad],
[straightUpRoad,lightGreyFloor,lightGreyFloor,lightGreyFloor2,straightUpRoad],
[straightUpRoad,lightGreyFloor2,lightGreyFloor2,lightGreyFloor,straightUpRoad],
[turnDownLeftRoad,staightSideRoad,staightSideRoad,staightSideRoad,turnDownRightRoad]]

level1 = Level("level1",(5,5))
level1.setLevel(levelrepr1)

while 1:
    level1.blitLevel(D)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    pygame.display.flip()