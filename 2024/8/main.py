import re

class Antenna:
    def __init__(self, YXCoord, frequency):
        self.YXCoord = YXCoord
        self.frequency = frequency

def filterAntennasByFrequency(antennaList, targetFrequenncy) -> list:
    filteredAntennas=[]
    for antenna in antennaList:
        if (antenna.frequency == targetFrequenncy):
            filteredAntennas.append(antenna)

    return filteredAntennas

def getAntinode(antenna, delta) -> list:
    return [antenna.YXCoord[0]+delta[0], antenna.YXCoord[1]+delta[1]]

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

def main():
    
    map = getMap()
    antennaList=[]
    for lineCount, lineElem in enumerate(map):
        for columnCount, columnElem in enumerate(lineElem):
            if(re.search("[a-z]|[A-Z]|[0-9]", columnElem) != None):
                antenna=Antenna([columnCount, lineCount], columnElem)
                print ("Antenna at :", antenna.YXCoord, ", frequency : ", antenna.frequency)
                antennaList.append(antenna)


    antinodeList=[]
    for antenna in antennaList:
        sameFrequenciesAntennas = filterAntennasByFrequency(antennaList, antenna.frequency)
        for neighborAntenna in sameFrequenciesAntennas:
            delta=[antenna.YXCoord[0] - neighborAntenna.YXCoord[0], antenna.YXCoord[1] - neighborAntenna.YXCoord[1]]
            if (delta[0] == 0 & delta[1] == 0):
                continue
            antinode=getAntinode(antenna, delta)
            if ((isOutOfBound(antinode,len(map), len(map[0])) == False) & (antinode not in antinodeList)):
                antinodeList.append(antinode)

    print (antinodeList)
    print ("antinode number : ", len(antinodeList))
    return 0



if __name__ == '__main__':
    main()