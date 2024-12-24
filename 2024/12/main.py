

from mapHelper import *
from getGroups import *

class PlantZone:
    def __init__(self, plots:list, type:str):
        self.plots = [plots]
        self.type = type
        self.regions = []

    def __str__(self):
        return f"plantZone type {self.type}"
    
    def getArea(self, region):
        return len(region)
    
    def getRegionPerimeter(self, region:list, mapSize:int)->int:
        totalRegionPerimeter = 0
        for coord in region:
            #print ("coord : ", coord)
            leftCoord=[coord[0], coord[1]-1]
            rightCoord=[coord[0], coord[1]+1]
            aboveCoord=[coord[0]-1, coord[1]]
            belowCoord=[coord[0]+1, coord[1]]

            #print (areAdjacents(coord, leftCoord, mapSize))
            #print (areAdjacents(coord, rightCoord, mapSize))
            #print (areAdjacents(coord, aboveCoord, mapSize))
            #print (areAdjacents(coord, belowCoord, mapSize))

            totalRegionPerimeter+=(4-((areAdjacents(coord, leftCoord, mapSize) & (leftCoord in region))
                                + (areAdjacents(coord, rightCoord, mapSize) & (rightCoord in region)) 
                                + (areAdjacents(coord, aboveCoord, mapSize) & (aboveCoord in region))
                                + (areAdjacents(coord, belowCoord, mapSize) & (belowCoord in region))
                                ))
            
        return totalRegionPerimeter
    
    def getPerimeter(self, mapSize:int)->int:
        totalPerimeter = 0
        for region in self.regions:
            totalPerimeter += self.getRegionPerimeter(region, mapSize)
        return totalPerimeter
    
    def getBarrierCost(self, mapSize:int)->int:
        total = 0
        for region in self.regions:
            #print (self.type, "- Area :", self.getArea(region), ", Perimeter :", self.getRegionPerimeter(region, mapSize))
            total += (self.getArea(region) * self.getRegionPerimeter(region, mapSize))
        return total

def getPlantZoneWithType(plantZoneList:list, targetType:str)->(PlantZone|None):
    for pZ in plantZoneList:
        if (pZ.type == targetType):
            return pZ
    return None

def main():

    plantZoneList=[]

    map=getMap()
    for y, lineElem in enumerate(map):
        for x, columnElem in enumerate(lineElem):
            if (any(plantZone.type == columnElem for plantZone in plantZoneList)):
                getPlantZoneWithType(plantZoneList, columnElem).plots.append([[x,y]])
            else:
                plantZoneList.append(PlantZone([[x,y]], columnElem))

    totalCost = 0
    for pZ in plantZoneList:
        print ("Plots : ", pZ.plots)
        pZ.regions = getGroupSOLUTION(pZ.plots, len(map[0]))
        print ("Regions :",pZ.regions)
        totalCost+=pZ.getBarrierCost(len(map[0]))
        print ("")


    print ("Total Cost :", totalCost)


    return 0

if __name__ == '__main__':
    main()