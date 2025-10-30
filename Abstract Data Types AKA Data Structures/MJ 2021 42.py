#part a)
class node():
    def __init__(self, data, node):
        self.data = data
        self.nextNode = node

#Part b)
LinkedList = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8), node(56,3),node(0,9), node(0,-1)]
startPointer = 0
emptyList = 5

#part c) i)
def outputNodes(LinkedList, startPointer):
    for x in range(len(LinkedList)):
        print(x, " - ", LinkedList[x].data, "|", LinkedList[x].nextNode)
    print("StartPointer: ", startPointer)

#Part c) ii)
outputNodes(LinkedList, startPointer)
print("---------------------------------------------------------------------")

#part d) i)
def addNode(LinkedList, startPointer, emptyList):
    if emptyList == -1:
        print("List is full!")
        return False

    item2add = int(input("Enter item to add: "))
    # 1. Get index of free node
    newNodePtr = emptyList
    # 2. Move emptyList to the next free node

    emptyList = LinkedList[emptyList].nextNode

    # 3. Fill in data for new node
    LinkedList[newNodePtr].data = item2add
    LinkedList[newNodePtr].nextNode = -1

    # 4. If list empty, update startPointer
    if startPointer == -1:
        startPointer = newNodePtr
    else:
        # Traverse to the end of the list
        current = startPointer
        while LinkedList[current].nextNode != -1:
            current = LinkedList[current].nextNode
        LinkedList[current].nextNode = newNodePtr
    return True

#part d) ii)
check = addNode(LinkedList, startPointer, emptyList)
if check:
    print("Node added successfully!")
else:
    print("Node not added!")

print("----------------------- after adding the node -----------------------")
outputNodes(LinkedList, startPointer)
