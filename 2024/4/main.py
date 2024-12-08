xMasLists = [
    [
        ['M', '_', 'S'],
        ['_', 'A', '_'],
        ['M', '_', 'S']
    ],[
        ['M', '_', 'M'],
        ['_', 'A', '_'],
        ['S', '_', 'S']
    ],[
        ['S', '_', 'M'],
        ['_', 'A', '_'],
        ['S', '_', 'M']
    ],[
        ['S', '_', 'S'],
        ['_', 'A', '_'],
        ['M', '_', 'M']
    ]
]

def hasMasPatternIn3x3Array(list3x3:list)->bool:
    for comparativePattern in xMasLists:
        if comparativePattern == list3x3:
            return True

def get3x3ArrayFromStartingPoint(startingPosition:list, doubleArray:list)->list:
    startingX=startingPosition[0]
    startingY=startingPosition[1]
    result=[
        [doubleArray[startingX-1][startingY-1], doubleArray[startingX-1][startingY], doubleArray[startingX-1][startingY+1]],
        [doubleArray[startingX][startingY-1],   doubleArray[startingX][startingY],   doubleArray[startingX][startingY+1]],
        [doubleArray[startingX+1][startingY-1], doubleArray[startingX+1][startingY], doubleArray[startingX+1][startingY+1]]
    ]
    return result

def parse3x3Array(list3x3:list)->list:
    list3x3[0][1] = '_'
    list3x3[1][0] = '_'
    list3x3[1][2] = '_'
    list3x3[2][1] = '_'
    return list3x3

def getCoordDeltaForHorizontalRight() -> list:
    return [[0,0],[0,1],[0,2],[0,3]]

def getCoordDeltaForHorizontalLeft() -> list:
    return [[0,0],[0,-1],[0,-2],[0,-3]]

def getCoordDeltaForVerticalDown() -> list:
    return [[0,0],[1,0],[2,0],[3,0]]

def getCoordDeltaForVerticalUp() -> list:
    return [[0,0],[-1,0],[-2,0],[-3,0]]

def getCoordDeltaForDiagonalDownRight() -> list:
    return [[0,0],[1,1],[2,2],[3,3]]

def getCoordDeltaForDiagonalDownLeft() -> list:
    return [[0,0],[1,-1],[2,-2],[3,-3]]

def getCoordDeltaForDiagonalUpRight() -> list:
    return [[0,0],[-1,1],[-2,2],[-3,3]]

def getCoordDeltaForDiagonalUpLeft() -> list:
    return [[0,0],[-1,-1],[-2,-2],[-3,-3]]

def getCombinationsMoves() -> list:
    return [
        getCoordDeltaForHorizontalRight(),
        getCoordDeltaForHorizontalLeft(),
        getCoordDeltaForVerticalDown(),
        getCoordDeltaForVerticalUp(),
        getCoordDeltaForDiagonalDownRight(),
        getCoordDeltaForDiagonalDownLeft(),
        getCoordDeltaForDiagonalUpRight(),
        getCoordDeltaForDiagonalUpLeft()
    ]

def getPossibleCombinationsMoves(arrayWidth:int, arrayHeight:int, startingPosition:list) -> list :
    wordSize=3 #XMAS is 4 letters, but we take in account the 0 in array
    startingY=startingPosition[0]
    startingX=startingPosition[1]
    moves=[]
    if ((startingX - wordSize)>=0):
        moves.append(getCoordDeltaForHorizontalLeft())
    if ((startingX + wordSize)<arrayWidth):
        moves.append(getCoordDeltaForHorizontalRight())
    if ((startingY - wordSize)>=0):
        moves.append(getCoordDeltaForVerticalUp())
    if ((startingY + wordSize)<arrayHeight):
        moves.append(getCoordDeltaForVerticalDown())

    if (((startingX - wordSize)>=0) & ((startingY + wordSize)<arrayHeight)):
        moves.append(getCoordDeltaForDiagonalDownLeft())
    if (((startingX + wordSize)<arrayWidth) & ((startingY + wordSize)<arrayHeight)):
        moves.append(getCoordDeltaForDiagonalDownRight())
    if (((startingX - wordSize)>=0) & ((startingY - wordSize)>=0)):
        moves.append(getCoordDeltaForDiagonalUpLeft())
    if (((startingX + wordSize)<arrayWidth) & ((startingY - wordSize)>=0)):
        moves.append(getCoordDeltaForDiagonalUpRight())
    
    return moves

def containsWordWithPattern(doubleArray:list, startingPosition:list, getCoordDeltaToCheck:list):
        isXLetter = doubleArray[startingPosition[0] + getCoordDeltaToCheck[0][0]][startingPosition[1] + getCoordDeltaToCheck[0][1]] == 'X' 
        isMLetter = doubleArray[startingPosition[0] + getCoordDeltaToCheck[1][0]][startingPosition[1] + getCoordDeltaToCheck[1][1]] == 'M'
        isALetter = doubleArray[startingPosition[0] + getCoordDeltaToCheck[2][0]][startingPosition[1] + getCoordDeltaToCheck[2][1]] == 'A'
        isSLetter = doubleArray[startingPosition[0] + getCoordDeltaToCheck[3][0]][startingPosition[1] + getCoordDeltaToCheck[3][1]] == 'S'
        
        if(isXLetter & isMLetter & isALetter & isSLetter):
            print ("XMAS at : ", startingPosition, "with ", getCoordDeltaToCheck)
        return isXLetter & isMLetter & isALetter & isSLetter

def main():

    inputArray=[]
    xMasCount=0
    masShapeXCount=0

    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            listedLine=list(line)
            if(listedLine[len(listedLine) -1] == '\n'):
                listedLine.pop(len(listedLine) -1)
            inputArray.append(listedLine)

    print (inputArray)

    for lineCount, lineElem in enumerate(inputArray):
        for columnCount, columnElem in enumerate(lineElem):
            if (columnElem == 'X'):
                startingPosition=[lineCount, columnCount]
                combinations = getPossibleCombinationsMoves(len(inputArray),len(inputArray[0]), startingPosition)
                for direction in combinations:
                    if (containsWordWithPattern(inputArray, startingPosition, direction)):
                        xMasCount+=1

    for lineCount, lineElem in enumerate(inputArray):
        if ((lineCount == 0) | (lineCount == len(inputArray)-1)):
            continue
        for columnCount, columnElem in enumerate(lineElem):
            if ((columnCount == 0) | (columnCount == len(inputArray[0])-1)):
                continue
            if (columnElem == 'A'):
                startingPosition=[lineCount, columnCount]
                print (startingPosition)
                array3x3 = parse3x3Array(get3x3ArrayFromStartingPoint(startingPosition, inputArray))
                if (hasMasPatternIn3x3Array(array3x3)):
                    masShapeXCount+=1

    print ("XMAS Count : ", xMasCount)    
    print ("Mas ShapeX Count : ", masShapeXCount)            

    return 0

if __name__ == '__main__':
    main()