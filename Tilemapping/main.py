# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import os
import math
from data import *

window = pygame.display.set_mode((windowWidth,windowHeight))
tileset = pygame.image.load(tilesetPath).convert()
world = Level(xTiles,yTiles,tileset,220)

for row in range(xTiles):
    for tile in range(yTiles):
        tileNumber = world.getTile(row,tile)
        
        xTilePos, yTilePos = tileNumber // tilesetWidth , tileNumber % tilesetWidth
        window.blit(tileset,(tile*tileWidth,row*tileHeight),tiles[xTilePos][yTilePos])
        
        
pygame.display.flip() 
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    