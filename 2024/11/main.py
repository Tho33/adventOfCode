def processOneBlink(peebleList:list)->list:
    newList = []
    for peeble in peebleList:
        if(int(peeble) == 0):
            newList.append(1)
        elif(len(str(peeble))%2 == 0):
            halfStringLength = len(str(peeble))//2
            firstPart=str(peeble)[:halfStringLength]
            secondPart=str(peeble)[halfStringLength:]
            newList.append(int(firstPart))
            newList.append(int(secondPart))
        else:
            newList.append(int(peeble)*2024)
    return newList

def main():

    inputList = []
    blinksToProcess = 75
    currentBlink = 0
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            inputList = line.split()

    nextList = inputList
    while (currentBlink != blinksToProcess):
        print ("Current blinking", currentBlink, "Out of ", blinksToProcess)
        nextList = processOneBlink(nextList)
        print ("ListSize :", len(nextList))
        currentBlink+=1

    print ("Final List : ", nextList)
    print ("Size : ", len(nextList))
    return 0

if __name__ == '__main__':
    main()