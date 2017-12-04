
def getDistanceFromCenter(i):
    n = 1
    level = 0
    x = 0
    y = 0

    while True:
        if i == pow(n, 2):
            return 2*level
        elif i < pow(n, 2):
            diff = (pow(n, 2) - i) % level
            return 2*level - diff
        level += 1
        n += 2


inputString = raw_input("Input data please: ")

y = getDistanceFromCenter(int(inputString))

print y