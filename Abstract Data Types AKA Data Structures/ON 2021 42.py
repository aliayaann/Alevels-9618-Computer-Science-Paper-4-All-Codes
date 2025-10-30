#binary tree stores integer data in ascending numerical order

# Each node has: [LeftPointer, Data, RightPointer]
ArrayNodes = [[ -1, -1, -1 ] for _ in range(20)]
RootPointer = -1
FreeNode = 0



def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the Data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = FreeNode
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")
    return RootPointer, FreeNode


def Printall():
    global RootPointer, FreeNode, ArrayNodes
    print("left | data | right")
    for x in range(20):
        print(ArrayNodes[x])

for i in range(10):
    RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)

Printall()
def InOrder(Root):
    global ArrayNodes
    if Root == -1:
        return
    InOrder(ArrayNodes[Root][0])  # left
    print(ArrayNodes[Root][1], end=" ")
    InOrder(ArrayNodes[Root][2])  # right

InOrder(RootPointer)
