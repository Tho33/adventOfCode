import re

def cleanBackspaces(line):
    clearedLine = line.replace('\n', '')
    return clearedLine


def main(argv):

    entryFile = open("./bag.txt","r")
    gamePowerSum = 0
    for line in entryFile:
        lineSplittedByTwoDots = line.split(':')
        gameSets = lineSplittedByTwoDots[1].split(';')
        colorMinimums = {
            "red":0,
            "green":0,
            "blue":0
        }
        for gameSet in gameSets:
            cubesRevealed = cleanBackspaces(gameSet).split(',')
            for colorSet in cubesRevealed:
                colorPair = colorSet.split()
                if int(colorPair[0]) > int(colorMinimums[colorPair[1]]):
                    colorMinimums[colorPair[1]]=int(colorPair[0])
        gamePowerSum = gamePowerSum + (colorMinimums["blue"] * colorMinimums["green"] * colorMinimums["red"])

    print(gamePowerSum)
    entryFile.close()
    return 0

if __name__ == '__main__':
    main(0)