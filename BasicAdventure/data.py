import pygame
from pygame.locals import *
from math import *
class Tileset:
    def __init__(self,tileset_img,tileSize,(xTiles,yTiles)):
        self.tileset_img = pygame.image.load(tileset_img).convert()
        self.tileSize = tileSize
        self.xTiles = xTiles
        self.yTiles = yTiles
        self.defRects()
        
    def defRects(self):
        self.rects = []
        for y in range(self.yTiles):
            self.rects.append([])
            for x in range(self.xTiles):
                startpoint = (x*self.tileSize,y*self.tileSize)
                endpoint = (startpoint[0]+32,startpoint[1]+32)
                self.rects[y].append(pygame.Rect(startpoint,(self.tileSize,self.tileSize)))
    
    def getRect(self,x,y):
        return self.rects[x][y]


class Level:
    def __init__(self,name,(longueur,largeur)):
        self.longueur, self.largeur = longueur,largeur
        self.initLevel()
    
    def initLevel(self):
        self.level = []
        for row in range(self.largeur):
            self.level.append([])
            for tile in range(self.longueur):
                self.level[row].append([])
    def setLevel(self,newLevel):
        self.level = newLevel
    
    def blitLevel(self,screen):
        for rown ,row in enumerate(self.level):
            for tilen,tile in enumerate(row):
                sourcetileset = tile.tileset
                source = sourcetileset.tileset_img
                size = sourcetileset.tileSize
                (ypos,xpos) = (tilen*size,rown*size)
                rect = tile.rect
                screen.blit(source,(ypos,xpos),rect)

"""
TILES !
"""



class GroundTile():
    def __init__(self,(y,x),tileset):
        self.tileset = tileset
        self.xPosInTileset = x
        self.yPosInTileset = y
        self.rect = self.tileset.getRect(self.yPosInTileset,self.xPosInTileset)

class LightGreyFloor(GroundTile):
    def __init__(self,tileset):
        GroundTile.__init__(self,(5,0),tileset)
        
        
class LightGreyFloor2(GroundTile):
    def __init__(self,tileset):
        GroundTile.__init__(self,(6,0),tileset)

class StraightUpRoad(GroundTile):
    def __init__(self,tileset):
        GroundTile.__init__(self,(1,4),tileset)

class StaightSideRoad(GroundTile):
    def __init__(self,tileset):
        GroundTile.__init__(self,(2,1),tileset)

class TurnUpLeftRoad(GroundTile):
    def __init__(self,tileset):
        GroundTile.__init__(self,(1,2),tileset)
class TurnUpRightRoad(GroundTile):
    def __init__(self,tileset):
        GroundTile.__init__(self,(1,3),tileset)
class TurnDownLeftRoad(GroundTile):
    def __init__(self,tileset):
        GroundTile.__init__(self,(2,2),tileset)
class TurnDownRightRoad(GroundTile):
    def __init__(self,tileset):
        GroundTile.__init__(self,(2,3),tileset)
"""
Levels !
"""