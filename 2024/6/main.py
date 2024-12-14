from helper import *
from getMap import *
from getGuardVisitedLocations import *

def main():

    map = getMap()
    result = getGuardVisitedLocations(map)
    if (len(result) != 0):
        locationsVisited = result[0]
        directionOnLocationsVisited = result[1]
        print ("Location Visited : ",len(locationsVisited))
        print ("Direction associees : ", len(directionOnLocationsVisited))

    alteredMaps = getAllAlteredMaps(map, locationsVisited)
    print ("Maps to process : ", len(alteredMaps))

    validAlternatedMaps = 0
    mapProcessed = 1

    for alteredMap in alteredMaps:
        print ("Map ", mapProcessed, " out of ", len(alteredMaps))
        mapProcessed+=1
        result = getGuardVisitedLocations(alteredMap)
        if (len(result) == 0):
            validAlternatedMaps+=1
    
    print ("Valid Alternated Maps found : ",validAlternatedMaps )





    

    return 0

if __name__ == '__main__':
    main()