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
    if (direction == Direction.RIGHT):
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


def main():

    map=[]

    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            listedLine=list(line)
            if(listedLine[len(listedLine) -1] == '\n'):
                listedLine.pop(len(listedLine) -1)
            map.append(listedLine)

    print (map)  
    guardLocation = coordsOfGuard(map)
    print (guardLocation)

    locationsVisited = [guardLocation]
    actualDirection = Direction.UP
    timeout=0

    while(timeout < 100):
        
        timeout+=1
        nextGuardLocation=getNextGuardLocation(guardLocation, actualDirection)
        print (guardLocation)
        if(isOutOfBound(nextGuardLocation, len(map), len(map[0]))):
            print ("END")
            break
            
            

        if(isObstacle(map[nextGuardLocation[1]][nextGuardLocation[0]])):
            actualDirection = goToNextDirection(actualDirection)
            print ("coucou", guardLocation, actualDirection)
            nextGuardLocation=getNextGuardLocation(guardLocation, actualDirection)
        

        locationsVisited.append(nextGuardLocation)
        guardLocation = nextGuardLocation





    

    return 0

if __name__ == '__main__':
    main()