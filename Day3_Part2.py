class SpiralCell:
    def __init__(self, xPos, yPos, value):
        self.xPos = xPos
        self.yPos = yPos
        self.value = value

    def getNextX(self, direction):
        if direction == 'R':
            return self.xPos+1
        elif direction == 'U':
            return self.xPos
        elif direction == 'L':
            return self.xPos-1
        else:
            return self.xPos

    def getNextY(self, direction):
        if direction == 'R':
            return self.yPos
        elif direction == 'U':
            return self.yPos+1
        elif direction == 'L':
            return self.yPos
        else:
            return self.yPos-1

    def toString(self):
        return "( " + str(self.xPos) + ", " + str(self.yPos) +", " + str(self.value) + " )"

    def setValue(self, value):
        self.value = value


def switchDir(direction):
    if direction == 'R':
        return 'U'
    elif direction == 'U':
        return 'L'
    elif direction == 'L':
        return 'D'
    else:
        return 'R'

def getAdjacentSum(spiralArr, cell):
    adjSum = 0
    for temp in spiralArr:
        if (temp.xPos == cell.xPos+1 and temp.yPos == cell.yPos) or (temp.xPos == cell.xPos+1 and temp.yPos == cell.yPos+1) or (temp.xPos == cell.xPos and temp.yPos == cell.yPos+1) or (temp.xPos == cell.xPos-1 and temp.yPos == cell.yPos+1) or (temp.xPos == cell.xPos-1 and temp.yPos == cell.yPos) or (temp.xPos == cell.xPos-1 and temp.yPos == cell.yPos-1) or (temp.xPos == cell.xPos and temp.yPos == cell.yPos-1) or (temp.xPos == cell.xPos+1 and temp.yPos == cell.yPos-1):
            adjSum += temp.value
    return adjSum


def getFirstLargerThan(inputInt):
    direction = 'R'
    xPos = 0
    yPos = 0
    begin = SpiralCell(0, 0, 1)
    spiralArr = list()
    spiralArr.append(begin)
    count = 1

    while True:
        for i in range(0, 2):
            for j in range(0, count):
                xPos = begin.getNextX(direction)
                yPos = begin.getNextY(direction)
                begin = SpiralCell(xPos, yPos, 0)
                value = getAdjacentSum(spiralArr, begin)
                if (value > inputInt):
                    return value
                else:
                    begin.setValue(value)
                    spiralArr.append(begin)
                j += 1
            direction = switchDir(direction)
        count += 1


inputInt = int(raw_input("Please enter int: "))
print(getFirstLargerThan(inputInt))

