def main():

    with open("input.txt", "r") as inputFile:
        uncompressedStringResult = []
        for line in inputFile:
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

            print (uncompressedStringResult)

            compressedListResult = uncompressedStringResult
            i = len(compressedListResult)-1

            while (i >= 0):
                print ("at ", i, " out of 0")
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

    print (compressedListResult)

    checkSum = 0
    for lineCount, elem in enumerate(compressedListResult):
        if (isinstance(elem, str)):
            break
        checkSum += (elem * lineCount)

    print ("checkSum : ", checkSum)

    return 0

if __name__ == '__main__':
    main()