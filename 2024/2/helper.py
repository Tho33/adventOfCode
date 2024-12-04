from enum import Enum

class FlowType(Enum):
    DECREASE = 1
    INCREASE = 2
    EQUAL = 3

def getInt(n) -> int :
    try:
        value = int(n)
        return value
    except ValueError:
        print(f"{n} is not a number")
        
def isDistanceAcceptable(level, nextLevel) -> bool:
    return abs(nextLevel - level) <= 3

def setupDirection(level, nextLevel) -> FlowType:
    if (level < nextLevel) :
        return FlowType.INCREASE
    elif (level > nextLevel) :
        return FlowType.DECREASE
    else :
        return FlowType.EQUAL

def isEndOfReport(nextIndex, report) -> bool:
    return (nextIndex) == len(report)

def getFixedReport(report, errorLevel) -> list:
    report.remove(errorLevel)
    return report

def isStepSafe(flowType:FlowType, level:int, nextLevel:int) -> bool:
    if(isDistanceAcceptable(level, nextLevel)):
        if ((flowType == FlowType.INCREASE) & (nextLevel > level)):
            return True
        elif ((flowType == FlowType.DECREASE) & (nextLevel < level)):
            return True
    return False

# report = line.split()
def isReportSafe(report:list) -> bool:
    i=-1
    for level in report:
        i+=1
        level=getInt(level)

        #End of report without error : OK
        if(isEndOfReport(i+1, report)):
            return True

        nextLevel=getInt(report[i+1])
        # Setup direction
        if (i == 0):
            flowType=setupDirection(level, nextLevel)
            if (flowType == FlowType.EQUAL):
                return False

        # Verify safety
        if (isStepSafe(flowType, level, nextLevel) == False):
            return False
        
def getFixedReports(report:list) -> list:
    result = []
    for index, level in enumerate(report):
        result.append(getFixedReport(report, index))
    return result

def getFixedReport(report:list, targetIndex:int) -> list:
    result=[]
    for index, level in enumerate(report):
        if (index != targetIndex):
            result.append(level)
    return result