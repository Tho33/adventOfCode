import re
def isMultiplyInstruction(line:str) -> bool:
    return re.search("mul\\([0-9]{1,3},[0-9]{1,3}\\)", line) != None

def isDoInstruction(line:str) -> bool:
    return re.search("do\\(\\)", line) != None

def isDontInstruction(line:str) -> bool:
    return re.search("don\\'t\\(\\)", line) != None

def getMultiplyListWithSwitches(line:str) -> list:
    return re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don\\'t\\(\\)",line)

def getMultiplyResult(list) -> int:
    return int(list[0]) * int(list[1])

def getMultiplyFactors(line:str) -> list:
    return re.findall("[0-9]{1,3}",line)

def main():

    multiplyList=[]
    sumResult=0
    doSwitch=1


    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            multiplyList = getMultiplyListWithSwitches(line)
            for elem in multiplyList:
                if(isDoInstruction(elem)):
                    doSwitch = 1
                if(isDontInstruction(elem)):
                    doSwitch = 0
                if(isMultiplyInstruction(elem)):
                    sumResult += doSwitch * getMultiplyResult(getMultiplyFactors(elem))

    print ("Result : ", sumResult)

    return 0

if __name__ == '__main__':
    main()