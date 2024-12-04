from helper import *

def main():

    safeReportCount = 0
    fixedReports = []
    wrongReports = []
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            report = line.split()
            if (isReportSafe(report)):
                safeReportCount += 1
            else :
                wrongReports.append(report)

    print("Bons reports : ", safeReportCount)
    print("Reports a revoir : ", len(wrongReports))
    print("~~")

    safeFixedReportsCount=0

    for report in wrongReports:
        fixedReports = getFixedReports(report)
        for fixedReport in fixedReports:
            if(isReportSafe(fixedReport)):
                safeFixedReportsCount += 1
                break

    print ("Bons reports : ", safeReportCount)
    print ("Bons reports fixes : ", safeFixedReportsCount)
    print ("Bons reports totaux : ", safeFixedReportsCount + safeReportCount)

    return 0

if __name__ == '__main__':
    main()