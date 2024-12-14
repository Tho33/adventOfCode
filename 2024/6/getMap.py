import copy

def getMap()->list:

    map=[]
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            listedLine=list(line)
            if(listedLine[len(listedLine) -1] == '\n'):
                listedLine.pop(len(listedLine) -1)
            map.append(listedLine)

    return map 

def getAllAlteredMaps(map:list, visitedLocations:list)-> list:
    alteredMaps = []
    mapCopied=0
    for lineCount, lineElem in enumerate(map):
        for columnCount, columnElem in enumerate(lineElem):
            if([columnCount, lineCount] not in visitedLocations):
                continue
            newMap = copy.deepcopy(map)
            print ("Maps Copied : ", mapCopied)
            mapCopied +=1
            if ((columnElem != '#') & (columnElem != '^')):
                newMap[lineCount][columnCount] = '#'
                alteredMaps.append(newMap)

    return alteredMaps

