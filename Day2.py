class Row:
    def __init__(self, rList):
        self.rList = sorted(rList, key=int, reverse=True)

    #part 1
    def getDifference(self):
        return max(self.rList) - min(self.rList)

    #part2
    def getEvenlyDifference(self):
        for i in range (0, len(self.rList)):
            num = self.rList[i]
            for x in range(i+1, len(self.rList)):
                if num % self.rList[x] == 0:
                    return num/self.rList[x]


# Initializing data from Day2_input
inputFile = open("Day2_input", "r")

checksum = 0

for line in inputFile:
    numbers = Row([int(i) for i in line.split()])

    #depending on the part, the fn will change here
    checksum += numbers.getEvenlyDifference()

print checksum
inputFile.close()



