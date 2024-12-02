from helper import *

def main():

    safeReportCount = 0
    fixedReports = []
    strangeList = []
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            report = line.split()
            i=-1
            for level in report:
                i+=1
                level=getInt(level)
                if(isEndOfReport(i+1, report)):
                    safeReportCount += 1
                    break
                nextLevel=getInt(report[i+1])

                # Setup direction
                if (i == 0):
                    flowType=setupDirection(level, nextLevel)
                    if (flowType == FlowType.EQUAL):
                        report.pop(i)
                        fixedReports.append(report)
                        break

                # Verify safety
                if (isStepSafe(flowType, level, nextLevel) == False):
                    if (i == 1):
                        strangeList.append(report)
                    report.pop(i+1)
                    fixedReports.append(report)
                    break

        
    print ("bons reports : ", safeReportCount)
    print ("Report a revoir : ", len(fixedReports))
    print(strangeList)

    safeFixedReportsCount=0

    for report in fixedReports:
        i=-1
        for level in report:
            i+=1
            level=getInt(level)
            if(isEndOfReport(i+1, report)):
                safeFixedReportsCount += 1
                break
            nextLevel=getInt(report[i+1])

            # Setup direction
            if (i == 0):
                flowType=setupDirection(level, nextLevel)
                if (flowType == FlowType.EQUAL):
                    break

            # Verify safety
            if (isStepSafe(flowType, level, nextLevel) == False):
                break

    print ("Bons reports : ", safeReportCount)
    print ("Bons reports fixés : ", safeFixedReportsCount)
    print ("Bons reports totaux : ", safeFixedReportsCount + safeReportCount)

    return 0

if __name__ == '__main__':
    main()