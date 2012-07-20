# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import os
import math
from data import *

window = pygame.display.set_mode((windowWidth,windowHeight))
tileset = pygame.image.load(tilesetPath).convert()
for row in range(xTiles):
    print "\n"
    for tile in range(yTiles):
        try:
            window.blit(tileset,(tile*tileWidth,row*tileHeight),tiles[int(world[row][tile])//len(tiles[0])][int(world[row][tile])-(int(world[row][tile])//len(tiles[0]))*len(tiles[0])])
        except:
            print "Error"
        
        
pygame.display.flip() 
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    