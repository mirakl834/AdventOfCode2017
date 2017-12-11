
inputFile = open("Day5_input", "r");

inputArray = [int(line) for line in inputFile];

goTo = 0;
countSteps = 0

while True:
    temp = inputArray[goTo]

    if temp >= 3:
        inputArray[goTo] -= 1
    else:
        inputArray[goTo] += 1

    goTo += temp
    countSteps += 1
    print(goTo)
    if (goTo < 0) or (goTo >= len(inputArray)):
        break

print(countSteps)
