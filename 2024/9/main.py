def getUncompressedPartition(line:str)-> list:
    uncompressedStringResult = []
    iD = 0
    hasToFill = True
    for digit in line:
        i = 0
        while (i< int(digit)):
            if (hasToFill == True):   
                uncompressedStringResult.append(iD)
            else:
                uncompressedStringResult.append('.')
            i+=1
        if (hasToFill == True):
            hasToFill = False
            iD +=1
        else:
            hasToFill = True
    return uncompressedStringResult

def getCompressedPartitionListFirstMethod(uncompressedPartitionList:list)-> list:
    compressedListResult = uncompressedPartitionList
    i = len(compressedListResult)-1
    while (i >= 0):
        print ("First Method : at ", i, " out of 0")
        digitToMove = compressedListResult[i]
        if (isinstance(digitToMove, int)):
            j=0
            while (isinstance(compressedListResult[j], int)):
                j+=1
            if (j > i):
                break
            compressedListResult[j] = digitToMove
            compressedListResult[i] = '.'
        i-=1
    return compressedListResult

def getPositionOfNContiguousFreeSpaces(compressedList:list, blockSizeTarget:int)->(int|None):
    currentBlockSize=0
    for cursor, elem in enumerate(compressedList):
        if (isinstance(elem, int)):
            currentBlockSize = 0
        else:
            currentBlockSize +=1
            if (currentBlockSize == blockSizeTarget):
                return cursor - blockSizeTarget + 1

        


def getCompressedPartitionListSecondMethod(uncompressedPartitionList:list)-> list:
    compressedListResult = uncompressedPartitionList
    endToStartCursor = len(compressedListResult)-1
    while (endToStartCursor >= 0):
        print ("Second Method : at ", endToStartCursor, " out of 0")
        digitToMove = compressedListResult[endToStartCursor]
        if (isinstance(digitToMove, int)):
            blockSize=0
            blockSizeCursor=endToStartCursor
            while ((isinstance(compressedListResult[blockSizeCursor], int)) & (compressedListResult[blockSizeCursor] == digitToMove)):
                blockSizeCursor-=1
                blockSize+=1
            freeSpaceCursor = getPositionOfNContiguousFreeSpaces(compressedListResult, blockSize)

            #print ("ID : ", digitToMove)
            #print ("blockSize : ", blockSize)
            #print ("freeSpaceCursor : ", freeSpaceCursor)
            #print ("blockSizeCursor : ", blockSizeCursor)

            if (freeSpaceCursor == None):
                #print (compressedListResult)
                endToStartCursor-=blockSize
                continue

            if (freeSpaceCursor > blockSizeCursor):
                #print (compressedListResult)
                endToStartCursor-=blockSize
                continue

            for i in range(blockSize):
                compressedListResult[freeSpaceCursor+i] = digitToMove
                compressedListResult[blockSizeCursor+i+1] = '.'
        #print (compressedListResult)
        endToStartCursor-=1

    return compressedListResult

def getCheckSum(compressedList)->int:
    checkSum = 0
    for lineCount, elem in enumerate(compressedList):
        if (isinstance(elem, str)):
            continue
        checkSum += (elem * lineCount)
    return checkSum

def main():

    uncompressedString = ""
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            uncompressedString = line

    uncompressedPartitionList1 = getUncompressedPartition(uncompressedString)
    uncompressedPartitionList2 = getUncompressedPartition(uncompressedString)
    print (uncompressedPartitionList1)
    print (uncompressedPartitionList2)

    compressedListResult1 = getCompressedPartitionListFirstMethod(uncompressedPartitionList1)
    print (compressedListResult1)

    compressedListResult2 = getCompressedPartitionListSecondMethod(uncompressedPartitionList2)
    print (compressedListResult2)

    checkSum1 = getCheckSum(compressedListResult1)
    checkSum2 = getCheckSum(compressedListResult2)
    print ("checkSum1 : ", checkSum1)
    print ("checkSum2 : ", checkSum2)

    return 0

if __name__ == '__main__':
    main()