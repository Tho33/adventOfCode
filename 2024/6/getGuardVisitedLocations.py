from helper import *

# Do the guard routine on the map in param
# returns a list :
# elem 0 : a list containing the visited Locations
# elem 1 : a list containing the associated directions
# list is empty if there is a loop in the guard patrolling routine
def getGuardVisitedLocations(map:list)->list :

    guardLocation = coordsOfGuard(map)
    locationsVisited = [guardLocation]
    actualDirection = Direction.UP
    locationAndDirections = [guardLocation, Direction.UP]

    while(True):
    
        #Guard checks in front of him
        nextGuardLocation=getNextGuardLocation(guardLocation, actualDirection)

        if([nextGuardLocation, actualDirection] in locationAndDirections):
            print ("Guard is in the loop !")
            return []

        if(isOutOfBound(nextGuardLocation, len(map), len(map[0]))):
            print ("END")
            break

        if(isObstacle(map[nextGuardLocation[1]][nextGuardLocation[0]])):
            actualDirection = goToNextDirection(actualDirection)
            locationAndDirections.append([guardLocation, actualDirection])
            nextGuardLocation=getNextGuardLocation(guardLocation, actualDirection)
            
            continue

        # Guard takes a step
        guardLocation = nextGuardLocation

        if (nextGuardLocation not in locationsVisited):
            locationsVisited.append(nextGuardLocation)
            locationAndDirections.append([nextGuardLocation, actualDirection])

    return [locationsVisited, locationAndDirections]

