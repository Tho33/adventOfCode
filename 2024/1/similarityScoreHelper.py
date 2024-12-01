def howManyIdenticTargetInList(list: list, target: int) -> int:
    count=0
    for x in list:
        if (x == target):
            count+=1
    return count

def getListSimilarityScore(listComputed: list, targetList: list) -> int:
    listSimilarityScore=0
    for x in listComputed:
        lineSimilarityScore=0
        sameValuesTotal=howManyIdenticTargetInList(targetList, x)
        lineSimilarityScore=x * sameValuesTotal
        listSimilarityScore+=lineSimilarityScore
    return listSimilarityScore