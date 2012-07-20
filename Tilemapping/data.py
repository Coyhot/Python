#-*-coding:utf-8 -*-

"""
Tilemapping data file
Contains all the data that the main file needs to perform the tilemapping
Created by coyhot
19/07/12 - */*/*
"""
tilesetPath = "files/tileset2.png"
tileHeight,tileWidth = 16,16 #Size of the tiles
xTiles,yTiles = 15,15 #Size of the level
windowHeight, windowWidth = tileHeight*xTiles,tileWidth*yTiles #*PROVISOIR* Window size from tiles
tilesetWidth,tilesetHeight = 43,25 #Number of tiles in the tileset
tileEspacement = 2 #The space in pixel between tiles
world = [
[0,1,2,3,4,5,6,7,9,10,11,12,13,14,15],
[16,17,18,19,20,21,23,24,25,26,27,28,29,30,31],
[32,33,34,35,36,37,38,39,40,41,42,43,45,44,46],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],
[47,48,49,50,51,52,53,54,55,56,57,58,59,60,61],] #Level representation 

tiles = [] #RECTS array
"""
RECTS creation for blitting
"""
for row in range(tilesetHeight):
    tiles.append([])
    for tile in range(tilesetWidth):
        tiles[row].append(((tileEspacement*(tile+1)+tileWidth*tile,tileEspacement*(row+1)+tileHeight*row),(tileEspacement*(tile+1)+tileWidth*tile+tileWidth,tileEspacement*(row+1)+tileHeight*row+tileHeight)))



