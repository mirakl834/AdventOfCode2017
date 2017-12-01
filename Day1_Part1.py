class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Initializing data input reader
inputString = raw_input("Input data please: ")

# Initializing the linked list
sumNum= 0
count = 0

while count < len(inputString):
    num1 = int(inputString[count])
    if count+1 == len(inputString):
        numNext = int(inputString[0])
    else:
        numNext = int(inputString[count + 1])

    if num1 == numNext:
        sumNum += num1
    count += 1

print(sumNum)







