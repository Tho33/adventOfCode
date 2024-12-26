from collections import defaultdict

def getPebblesFromPebble(pebble:int)->list[str]:
        
        if(int(pebble) == 0):
            return ["1"]
        
        if(len(str(int(pebble)))%2 == 0):
            halfStringLength = len(str(pebble))//2
            firstPart=str(pebble)[:halfStringLength]
            secondPart=str(pebble)[halfStringLength:]
            return [str(int(firstPart)), str(int(secondPart))]
        
        return [str(int(pebble)*2024)]

def main():

    inputList = []
    blinksToProcess = 75
    currentBlink = 0
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            inputList = line.split()

    initialDict = defaultdict(int)
    for pebble in inputList:
        initialDict[pebble]+=1

    print (initialDict)
    
    while (currentBlink != blinksToProcess):
        print ("Current blinking", currentBlink, "Out of ", blinksToProcess)
        newPebbleDict = defaultdict(int)

        for pebble, quantity in initialDict.items():
            for newPebble in getPebblesFromPebble(pebble):
                newPebbleDict[newPebble]+=quantity

        currentBlink+=1
        initialDict = newPebbleDict

    result = 0
    for pebble, quantity in initialDict.items():
        result+= quantity

    print ("Total of pebbles :", result)

    return 0

if __name__ == '__main__':
    main()