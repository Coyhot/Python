#-*-coding:utf-8 -*-

"""
Tilemapping data file
Contains all the data that the main file needs to perform the tilemapping
Created by coyhot
19/07/12 - */*/*
"""
tileHeight,tileWidth = 16,16 #Size of the tiles
xTiles,yTiles = 15,15 #Size of the level
windowHeight, windowWidth = tileHeight*xTiles,tileWidth*yTiles #*PROVISOIR* Window size from tiles
tilesetWidth,tilesetHeight = 8,6 #Number of tiles in the tileset
tileEspacement = 2 #The space in pixel between tiles


tiles = [] #RECTS array
"""
RECTS creation for blitting
"""
for row in range(tilesetHeight):
    tiles.append([])
    for tile in range(tilesetWidth):
        tiles[row].append(((tileEspacement*(tile+1)+tileWidth*tile,tileEspacement*(row+1)+tileHeight*row),(tileEspacement*(tile+1)+tileWidth*tile+tileWidth,tileEspacement*(row+1)+tileHeight*row+tileHeight)))



class Level:
    def __init__(self,height,width,tileset, basetile = 0):
        self.height = height
        self.width = width
        self.tileset = tileset
        self.basetile = basetile
        self.generateBaseArray()
    
    def generateBaseArray(self):
        self.level = []
        for a in range(self.height):
            self.level.append([])
            for b in range(self.width):
                self.level[a].append(self.basetile)
    
    def getTile(self,x,y):
        return self.level[x][y]
    
    def setTile(self,x,y,number):
        self.level[x][y] = number
    def printTTY(self):
        print self.level
    
    def display(self,surface):
        for row in range(xTiles):
            for tile in range(yTiles):
                self.tileNumber = self.getTile(row,tile)
                
                self.xTilePos, self.yTilePos = self.tileNumber // tilesetWidth , self.tileNumber % tilesetWidth
                surface.blit(self.tileset,(tile*tileWidth,row*tileHeight),tiles[self.xTilePos][self.yTilePos])
        



