def getListsFromFile(file) -> list:
    leftColumn=[]
    rightColumn=[]
    for line in file:
        lineList=line.split()
        leftVal=getInt(lineList[0])
        rightVal=getInt(lineList[1])

        if (leftVal != False):
            leftColumn.append(leftVal)
        if (rightVal != False):
            rightColumn.append(rightVal)
        
    leftColumn.sort()
    rightColumn.sort()

    return [leftColumn, rightColumn]

def getAbsoluteValueBetweenTwoLists(list1, list2) -> int:
    result=0
    if(len(list1) - len(list2) != 0):
        print("error, size column differents")
        print (len(list1) - len(list2))
    
    for x in range(len(list1)):
        result+=abs(list1[x] - list2[x])
    return result

def getInt(n) -> int | bool:
    try:
        value = int(n)
        return value
    except ValueError:
        print(f"{n} is not a number")
        return False
