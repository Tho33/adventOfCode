import re

def convertToRealNumber(value):
    valueCorresponder = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    if len(value) != 1:
        return valueCorresponder[str(value)]
    else:
        return value

def main(argv):

    entryFile = open("./calibrationFile.txt","r")
    calibrationSum=0
    for line in entryFile:
        numbersDetected = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))", line)
        firstDigit = numbersDetected[0]
        lastDigit = numbersDetected[len(numbersDetected)-1]
        firstDigit = convertToRealNumber(firstDigit)
        lastDigit = convertToRealNumber(lastDigit)
        calibrationPoint = str(firstDigit)+str(lastDigit)
        print (calibrationPoint)
        calibrationSum = calibrationSum+int(calibrationPoint)

    print(calibrationSum)    
    entryFile.close()
    return 0

if __name__ == '__main__':
    main(0)