import itertools

line = "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"

combos = set()
comboList = list()

inputArray = [int(i) for i in line.split()]

maximum = max(inputArray)
distribution = maximum
isDist = False
distCount = 0
oldLen = -1

print(maximum)
while True:
    for i in range(0, len(inputArray)):
        if isDist is False:
            if inputArray[i] == maximum:
                print(str(inputArray[i]) + " is max")
                inputArray[i] = 0
                isDist = True
                distCount += 1
        else:
            if distribution is not 0:
                print("dstributing")
                inputArray[i] += 1
                distribution -= 1
            else:
                maximum = max(inputArray)
                distribution = maximum
                print("new max is " + str(maximum))
                isDist = False
                oldLen = len(combos)
                print(str(inputArray))
                combos.add(str(inputArray))
                comboList.append(str(inputArray))
                break;
    if oldLen == len(combos):
        strIndex = comboList.index(str(inputArray))
        interval = len(comboList) - strIndex-1
        print(interval)
        break;

print(distCount)
