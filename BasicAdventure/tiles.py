
class Tile:
    def __init__(self,(y,x),tileset):
        self.xPosInTileset = x
        self.yPosInTileset = y
        self.tileset = tileset

class GroundTile(Tile):
    def __init__(self,(y,x),tileset):
        Tile.__init__(self,(x,y),tileset)

class LightGreyFloor:
    def __init__(self,(y,x)):
        self.xPosInTileset = x
        self.yPosInTileset = y
        self.rect = baseTileset.getRect(self.yPosInTileset,self.xPosInTileset)
lightGreyFloor = LightGreyFloor((5,0))