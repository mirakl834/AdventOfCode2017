class Row:
    def __init__(self, rList):
        self.rList = rList

    #Part 1
    def isValid(self):
        for i in range(0, len(self.rList)):
            word = str(self.rList[i])
            for x in range(i+1, len(self.rList)):
                if word == str(self.rList[x]):
                    return False
        return True

    def isValidPlus(self):
        for i in range(0, len(self.rList)):
            word = ''.join(sorted(str(self.rList[i])))
            for x in range(i+1, len(self.rList)):
                if word == ''.join(sorted(str(self.rList[x]))):
                    return False
        return True

inputFile = open("Day4_input", "r")
validCount = 0

for line in inputFile:
    passphrase = Row(line.split())
    if passphrase.isValidPlus():
        validCount += 1

print(validCount)
