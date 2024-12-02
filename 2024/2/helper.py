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