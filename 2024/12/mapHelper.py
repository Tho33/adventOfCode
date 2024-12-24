def getMap()->list:

    map=[]
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            listedLine=list(line)
            if(listedLine[len(listedLine) -1] == '\n'):
                listedLine.pop(len(listedLine) -1)
            map.append(listedLine)
    return map 

def getXY(x:int,y:int,map:list):
    return map[y][x]

def getAbove(x:int, y:int, map:list)->list:
    return map[y-1][x]

def getBelow(x:int, y:int, map:list)->list:
    return map[y+1][x]

def getLeft(x:int, y:int, map:list)->list:
    return map[y][x-1]

def getRight(x:int, y:int, map:list)->list:
    return map[y][x+1]

def areAdjacents(node1:list, node2:list, mapSize:int):
    right = False
    left = False
    up = False
    down = False
    if (isOutOfBound([node1[0]+1, node1[1]], mapSize, mapSize) == False):
        right = (node1[0]+1 == node2[0]) & (node1[1] == node2[1])
    if (isOutOfBound([node1[0]-1, node1[1]], mapSize, mapSize) == False):
        left = (node1[0]-1 == node2[0]) & (node1[1] == node2[1])
    if (isOutOfBound([node1[0], node1[1]+1], mapSize, mapSize) == False):
        down = (node1[1]+1 == node2[1]) & (node1[0] == node2[0])
    if (isOutOfBound([node1[0], node1[1]-1], mapSize, mapSize) == False):
        up = (node1[1]-1 == node2[1]) & (node1[0] == node2[0])
    return (right | left | down | up)

def isOutOfBound(coords:list, mapWidth:int, mapHeight:int)-> bool:
    return (
            ((coords[0] < 0 ) | (coords[0] >= mapHeight)) |
            ((coords[1] < 0 ) | (coords[1] >= mapWidth))
    )