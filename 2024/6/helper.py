from enum import Enum

class Direction(Enum):

    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

coordDeltaByDirection = {
    Direction.UP:   [0,-1],
    Direction.RIGHT:[1,0],
    Direction.DOWN: [0,1],
    Direction.LEFT: [-1,0]
}

def goToNextDirection(direction:Direction)-> Direction:
    if (direction == Direction.UP):
        return Direction.RIGHT
    if (direction == Direction.RIGHT):
        return Direction.DOWN
    if (direction == Direction.DOWN):
        return Direction.LEFT
    if (direction == Direction.LEFT):
        return Direction.UP

def isObstacle(character:str)-> bool:
    return character == '#'

def isOutOfBound(coords:list, mapWidth:int, mapHeight:int)-> bool:
    return (
            ((coords[0] < 0 ) | (coords[0] >= mapHeight)) |
            ((coords[1] < 0 ) | (coords[1] >= mapWidth))
    )

def coordsOfGuard(map:list)->list:
    for lineCount, lineElem in enumerate(map):
        for columnCount, columnElem in enumerate(lineElem):
            if (columnElem == '^'):
                return [columnCount, lineCount]
            
def getNextGuardLocation(guardLocation:list, direction:Direction):
    return [guardLocation[0]+coordDeltaByDirection[direction][0], guardLocation[1]+coordDeltaByDirection[direction][1]]