from similarityScoreHelper import *
from distanceScoreHelper import *

def main(argv):

    with open("input.txt", "r") as inputFile:
        result = getListsFromFile(inputFile)
        leftColumn = result[0]
        rightColumn = result[1]

    result1=getAbsoluteValueBetweenTwoLists(leftColumn, rightColumn)
    result2=getListSimilarityScore(leftColumn, rightColumn)

    print("result 1.1 : ",result1)
    print("result 1.2 : ", result2)

    return 0

if __name__ == '__main__':
    main(0)