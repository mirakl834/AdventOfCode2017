import itertools

class Node:
    def __init__(self, value, weight, children):
        self.value = value
        self.weight = int(weight)
        self.children = children

    def setChildren(self,children):
        self.children = children

    def getValue(self):
        return self.value

    def isMyChild(self, node):
        for child in self.children:
            if(child == node.getValue()):
                return True
        return False

    def hasChildren(self):
        if not self.children:
            return False
        else:
            return True

    def printNode(self):
        print(node.getValue() + "| w: "+ str(self.weight))

    def getWeight(self):
        return self.weight

    def getTotalWeight(self):
        total = self.weight
        if self.hasChildren():
            for child in self.children:
                total += child.getTotalWeight()
        return total

inputFile = open("Day7_input", "r");

nodeList = list()

for line in inputFile:
    words = [i.strip(',') for i in line.split()]
    value = words[0]
    weight = words[1].strip('(').strip(')')
    if len(words)> 2:
        children = words[3:]
    else:
        children = []
    nodeList.append(Node(value, weight, children))


for node in nodeList:
    if node.hasChildren():
        isChild = False
        for compareNode in nodeList:
            if compareNode.hasChildren():
                if compareNode.isMyChild(node):
                    isChild = True
                    break;
        if not isChild:
            root = node
            print(node.getValue())

def getNodeChildren(node, nodelist):
    nodeChildren = list()
    for compareNode in nodelist:
        if node.isMyChild(compareNode):
            nodeChildren.append(compareNode)
    return nodeChildren

def generateTree(root):
    root.setChildren(getNodeChildren(root, nodeList))
    for child in root.children:
        if child.hasChildren():
            generateTree(child)


generateTree(root)

def getFaultyWeight(root):
    weightSet = set()
    for i in range(0, len(root.children)):
        child = root.children[i]
        weightSet.add(child.getTotalWeight())
        if len(weightSet) > 1:
            print(child.weight)
            getFaultyWeight(child)
            break;


getFaultyWeight(root)

for child in root.children:
    print(child.getTotalWeight())









