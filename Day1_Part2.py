# Initializing data input reader
inputString = raw_input("Input data please: ")

# Initializing the linked list
sumNum = 0
count = 0
length = len(inputString)
half = length/2

while count < length:
    num1 = int(inputString[count])
    halfIndex = count + half

    if halfIndex >= length:
        numNext = int(inputString[(halfIndex - length)])
    else:
        numNext = int(inputString[halfIndex])

    if num1 == numNext:
        sumNum += num1
    count += 1

print(sumNum)







