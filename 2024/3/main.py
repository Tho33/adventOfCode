import re
def getMultiplyList(line:str) -> list:
    return re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",line)

def getMultiplyResult(list) -> int:
    return int(list[0]) * int(list[1])

def main():

    multiplyList=[]
    sumResult=0

    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            multiplyList = getMultiplyList(line)

    for elem in multiplyList:
        numbersToMultiply = re.findall("[0-9]{1,3}",elem)
        sumResult += getMultiplyResult(numbersToMultiply)
        print (elem, getMultiplyResult(numbersToMultiply))
    print (sumResult)


    return 0

if __name__ == '__main__':
    main()