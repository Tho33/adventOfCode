totalTrailHeadScore=0
trailheadSummitsPositions=[]

def getMap():

    map = []
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            listedLine=list(line)
            if(listedLine[len(listedLine) -1] == '\n'):
                listedLine.pop(len(listedLine) -1)
            map.append(listedLine)
    return map

def isOutOfBound(coords:list, mapWidth:int, mapHeight:int)-> bool:
    return (
            ((coords[0] < 0 ) | (coords[0] >= mapHeight)) |
            ((coords[1] < 0 ) | (coords[1] >= mapWidth))
    )

def getPath(x:int, y:int, map:list, target:int):
    mapSize = len(map)
    global totalTrailHeadScore

    if (target == 10):
        print ("At x: ", x, " y: ",y, ", its the summit !")
        return 1
    else:
        # Go Right
        if(isOutOfBound([y, x+1], mapSize, mapSize) == False):
            if (int(map[y][x+1]) == int(target)):
                print ("At x: ", x, " y: ",y, ", target :" , target," we go right.")
                if (getPath(x+1, y, map, target+1) == 1):
                    if ([y, x+1] not in trailheadSummitsPositions):
                        trailheadSummitsPositions.append([y,x+1])
                        totalTrailHeadScore+=1
        # Go Left
        if(isOutOfBound([y, x-1], mapSize, mapSize) == False):
            if (int(map[y][x-1]) == int(target)):
                print ("At x: ", x, " y: ",y, ", target :" , target," we go left.")
                if (getPath(x-1, y, map, target+1) == 1):
                    if ([y, x-1] not in trailheadSummitsPositions):
                        trailheadSummitsPositions.append([y,x-1])
                        totalTrailHeadScore+=1
        # Go Up
        if(isOutOfBound([y-1, x], mapSize, mapSize) == False):
            if (int(map[y-1][x]) == int(target)):
                print ("At x: ", x, " y: ",y, ", target :" , target," we go up.")
                if (getPath(x, y-1, map, target+1) == 1):
                    if ([y-1, x] not in trailheadSummitsPositions):
                        trailheadSummitsPositions.append([y-1,x])
                        totalTrailHeadScore+=1
        # Go Down
        if(isOutOfBound([y+1, x], mapSize, mapSize) == False):
            if (int(map[y+1][x]) == int(target)):
                print ("At x: ", x, " y: ",y, ", target :" , target," we go down.")
                if (getPath(x, y+1, map, target+1) == 1):
                    if ([y+1, x] not in trailheadSummitsPositions):
                        trailheadSummitsPositions.append([y+1,x])
                        totalTrailHeadScore+=1

    return 0

def getPathRating(x:int, y:int, map:list, target:int):
    mapSize = len(map)
    global totalTrailHeadScore

    if (target == 10):
        print ("At x: ", x, " y: ",y, ", its the summit !")
        return 1
    else:
        # Go Right
        if(isOutOfBound([y, x+1], mapSize, mapSize) == False):
            if (int(map[y][x+1]) == int(target)):
                print ("At x: ", x, " y: ",y, ", target :" , target," we go right.")
                if (getPathRating(x+1, y, map, target+1) == 1):
                    totalTrailHeadScore+=1
        # Go Left
        if(isOutOfBound([y, x-1], mapSize, mapSize) == False):
            if (int(map[y][x-1]) == int(target)):
                print ("At x: ", x, " y: ",y, ", target :" , target," we go left.")
                if (getPathRating(x-1, y, map, target+1) == 1):
                    totalTrailHeadScore+=1
        # Go Up
        if(isOutOfBound([y-1, x], mapSize, mapSize) == False):
            if (int(map[y-1][x]) == int(target)):
                print ("At x: ", x, " y: ",y, ", target :" , target," we go up.")
                if (getPathRating(x, y-1, map, target+1) == 1):
                    totalTrailHeadScore+=1
        # Go Down
        if(isOutOfBound([y+1, x], mapSize, mapSize) == False):
            if (int(map[y+1][x]) == int(target)):
                print ("At x: ", x, " y: ",y, ", target :" , target," we go down.")
                if (getPathRating(x, y+1, map, target+1) == 1):
                    totalTrailHeadScore+=1

    return 0

def main():

    map = getMap()
    global totalTrailHeadScore
    global trailheadSummitsPositions

    score = 0
    rating = 0
        
    for y, lineElem in enumerate(map):
        for x, columnElem in enumerate(lineElem):
            if (int(columnElem) == 0):
                getPath(x, y, map, 1)
                score += totalTrailHeadScore
                totalTrailHeadScore = 0
                trailheadSummitsPositions = []

    for y, lineElem in enumerate(map):
        for x, columnElem in enumerate(lineElem):
            if (int(columnElem) == 0):
                getPathRating(x, y, map, 1)
                rating += totalTrailHeadScore
                totalTrailHeadScore = 0

    print (score)
    print (rating)
    return 0

if __name__ == '__main__':
    main()