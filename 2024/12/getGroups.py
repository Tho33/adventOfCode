from mapHelper import *

iterationCount = 0

# Run over small 1-group
# If find one group adjacent to another, add it together, delete one, and run it again
def getGroupTOOLONG(groupsList:list, mapSize:int):
    global iterationCount
    iterationCount+=1
    print (iterationCount)
    for group in groupsList:
        for coord in group:
            # print ("coord:", coord, ", first : ",groupList)
            for groupList in groupsList:
                if (groupList == group):
                    continue
                for workingCoord in groupList:
                    if (areAdjacents(coord, workingCoord, mapSize) == True):
                        groupList.extend(group)
                        groupsList.remove(group)
                        return getGroupTOOLONG(groupsList, mapSize)

    return groupsList


def areAdjacents(coord1, coord2, mapSize):
    # Vérifie si deux coordonnées sont adjacentes (orthogonalement)
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) + abs(y1 - y2) == 1

def getGroupSOLUTION(groupsList, mapSize):
    visited = set()  # Ensemble pour suivre les coordonnées déjà visitées
    result = []  # Liste des groupes finaux

    # Transforme les groupes en un seul ensemble de coordonnées à parcourir
    all_coords = [coord for group in groupsList for coord in group]

    for coord in all_coords:
        if tuple(coord) in visited:
            continue  # Ignore les coordonnées déjà regroupées

        # Nouvelle composante connexe
        group = []
        stack = [coord]

        while stack:
            current = stack.pop()
            if tuple(current) in visited:
                continue
            visited.add(tuple(current))
            group.append(current)

            # Ajoute les voisins adjacents non visités
            for other in all_coords:
                if tuple(other) not in visited and areAdjacents(current, other, mapSize):
                    stack.append(other)

        result.append(group)

    return result