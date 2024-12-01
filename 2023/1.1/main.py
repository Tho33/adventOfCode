import re

def main(argv):

    entryFile = open("./calibrationFile.txt","r")
    calibrationSum=0
    for line in entryFile:
        numbersDetected = re.findall("[0-9]", line)
        firstDigit = numbersDetected[0]
        lastDigit = numbersDetected[len(numbersDetected)-1]
        calibrationPoint = firstDigit+lastDigit
        calibrationSum = calibrationSum+int(calibrationPoint)

    print(calibrationSum)    
    entryFile.close()
    return 0

if __name__ == '__main__':
    main(0)