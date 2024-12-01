import re
from schematicLineClass import SchematicLine
from schematicLineClass import NumberWithPosition

def cleanBackspaces(line):
    clearedLine = line.replace('\n', '')
    return clearedLine

def isSymbol(character):
    return len(re.findall(r"[^0-9\.\n]", str(character))) > 0
    
def isNumber(character):
    return len(re.findall("[0-9]", character)) > 0

def getNumbersWithPosition(schematicLine):
    result = []
    position=-1
    topNumber=0
    value=''
    for character in schematicLine:
        position=position+1
        if topNumber==0:
            if isNumber(character):
                topNumber=1
                value=value+character
        else :
            if isNumber(character):
                value=value+character
            else:
                topNumber=0
                result.append(NumberWithPosition(value, position-len(value)))
                value=''
    return result

def getPositionsToCheck(numberWithPosition):
    result = []
    for i in range(numberWithPosition.position-1, numberWithPosition.position+1+len(numberWithPosition.value)):
        result.append(i)
    return result

def main(argv):

    entryFile = open("./schematic.txt","r")
    schematicSum = 0
    schematicArray=[]
    id=0
    for line in entryFile:
        id=id+1
        schematicArray.append(SchematicLine(id, line))
    
    numbersWithPosition=[]
    for schematicLine in schematicArray:
        numbersWithPosition.append(getNumbersWithPosition(schematicLine.line))

    i=-1
    for elem in numbersWithPosition:
        i=i+1
        for group in elem:
            topCheck=0
            lineToCheck=[]
            # initialisation des lignes
            if(i-1 >= 0):
                lineToCheck.append(schematicArray[i-1])
            lineToCheck.append(schematicArray[i])
            if(i+1<=139):
                lineToCheck.append(schematicArray[i+1])

            # Check Symbol
            positionToCheck = getPositionsToCheck(group)
            for line in lineToCheck:
                for pos in positionToCheck:
                    if pos >= 0 :
                        if (isSymbol(line.line[pos])):
                            print("space ? ", group.value, line.line[pos])
                            topCheck=1

            if topCheck==1:
                topCheck=0
                schematicSum=schematicSum+int(group.value)

    print (schematicSum)
    return 0

if __name__ == '__main__':
    main(0)