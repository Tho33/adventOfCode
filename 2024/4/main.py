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
    startingX=startingPosition[0]
    startingY=startingPosition[1]
    moves=[]
    if (startingX - wordSize)>=0:
        moves.append(getCoordDeltaForHorizontalLeft())
    if (startingX + wordSize)<arrayWidth:
        moves.append(getCoordDeltaForHorizontalRight())
    if (startingY - wordSize)>=0:
        moves.append(getCoordDeltaForVerticalUp())
    if (startingY + wordSize)<arrayHeight:
        moves.append(getCoordDeltaForVerticalDown())

    return moves

def containsWordWithPattern(doubleArray:list, startingPosition:list, getCoordDeltaToCheck:list):
        isXLetter = doubleArray[startingPosition[0] + getCoordDeltaToCheck[0][0]][startingPosition[1] + getCoordDeltaToCheck[0][1]] == 'X' 
        isMLetter = doubleArray[startingPosition[0] + getCoordDeltaToCheck[1][0]][startingPosition[1] + getCoordDeltaToCheck[1][1]] == 'M'
        isALetter = doubleArray[startingPosition[0] + getCoordDeltaToCheck[2][0]][startingPosition[1] + getCoordDeltaToCheck[2][1]] == 'A'
        isSLetter = doubleArray[startingPosition[0] + getCoordDeltaToCheck[3][0]][startingPosition[1] + getCoordDeltaToCheck[3][1]] == 'S'
        
        return isXLetter & isMLetter & isALetter & isSLetter

def main():

    inputArray=[]
    count=0

    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            listedLine=list(line)
            listedLine.pop(len(listedLine) -1)
            inputArray.append(listedLine)

    print (inputArray)

    for lineCount, lineElem in enumerate(inputArray):
        for columnCount, columnElem in enumerate(lineElem):
            if (columnElem == 'X'):
                startingPosition=[lineCount, columnCount]
                combinations = getPossibleCombinationsMoves(len(inputArray),len(inputArray[0]), startingPosition)
                for direction in combinations:
                    print ("direction : ", direction)
                    print ("start : ", startingPosition)
                    if (containsWordWithPattern(inputArray, startingPosition, direction)):
                        count+=1


    return 0

if __name__ == '__main__':
    main()