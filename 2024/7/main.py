import re
import itertools

def getOperatorsCombination(arraySize)->list:
    return list(itertools.product('*+|', repeat=arraySize-1))

def getPossibleCombinations(components:list)->list:
    operatorCombinations = getOperatorsCombination(len(components))
    result = 0
    resultList=[]
    for operatorCombination in operatorCombinations:
        for index, component in enumerate(components):
            if (index == 0):
                result = component
            else :
                if (operatorCombination[index - 1] == '*'):
                    result = result * component
                elif (operatorCombination[index - 1] == '+'):
                    result = result + component
                elif (operatorCombination[index - 1] == '|'):
                    result = int(str(result) + str(component))
        resultList.append(result)    
    return resultList

def main():

    total = 0

    count = 0

    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            count += 1
            firstPart = re.search("^.*:", line).group()
            firstPart = firstPart[:len(firstPart)-1]
            lastPart = re.search("[^:]*$", line).group()[1:]

            target = int(firstPart)
            components = list(map(int,lastPart.split()))

            print ("calculate no ", count, " out of ", 850)

            if (target in getPossibleCombinations(components)):
                total = total + target

    print ("result : ", total)

    return 0

if __name__ == '__main__':
    main()