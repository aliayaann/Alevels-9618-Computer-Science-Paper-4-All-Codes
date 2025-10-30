# --------- Question.1 ---------
#Part (a)
Queue = [-1 for _ in range(20)]
HeadPointer = -1
TailPointer = -1
NumberItems = 0

#Part (b)
def Enqueue(Num2Add):
    global HeadPointer, TailPointer, NumberItems
    if NumberItems == 20:
        return False
    else:
        if HeadPointer == -1:
            HeadPointer = 0
        TailPointer += 1
        Queue[TailPointer] = Num2Add
        NumberItems += 1
        return True

#Part (c)
for x in range(1,26):
    if Enqueue(x):
        print(x,"Successfull")
    else:
        print(x,"Unsuccessfull")

#Part (d)
def Dequeue():
    global HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
        return -1
    else:
        HeadPointer += 1
        NumberItems -= 1
        return Queue[HeadPointer]

#Part (e)
for x in range(2):
    print("The First Element of the Queue now is: ",Dequeue())

# --------- Question.2 ---------
#Part (a):
def ReadData():
    DataArray = []
    FileName = input("Enter file name: ")
    with open(f"C:\\Users\\aliay\\Desktop\\Text Files\\9618_s25_sf_41\\{FileName}", 'r') as File:
        for line in File:
            DataArray.append(line.strip())
    return DataArray


#Part (b):
def SplitData(DataArray):
    Red = []
    Blue = []
    Green = []
    Yellow = []
    Orange = []
    Pink = []

    for Line in DataArray:
        Parts = Line.split(",")
        if Parts[1] == "red":
            Red.append(int(Parts[0]))
        elif Parts[1] == "blue":
            Blue.append(int(Parts[0]))
        elif Parts[1] == "green":
            Green.append(int(Parts[0]))
        elif Parts[1] == "yellow":
            Yellow.append(int(Parts[0]))
        elif Parts[1] == "orange":
            Orange.append(int(Parts[0]))
        else:
            Pink.append(int(Parts[0]))

# Part (d):
    StoreData(Red, "Red.txt")
    StoreData(Blue, "Blue.txt")
    StoreData(Green, "Green.txt")
    StoreData(Yellow, "Yellow.txt")
    StoreData(Orange, "Orange.txt")
    StoreData(Pink, "Pink.txt")

#Part (c):
def StoreData(DataToStore, FileName):
    try:
        with open(rf"C:\\Users\\aliay\\Desktop\\Text Files\\9618_s25_sf_41\\{FileName}", 'a') as File:
            for item in DataToStore:
                File.write(str(item)+"\n")
        print("Data Stored Successfully in",FileName)
    except:
        IOError("Something went wrong")

output = ReadData()
print(output)
SplitData(output)


# --------- Question 3 ---------

#Part (a)
#(i)
class Node:
    # PRIVATE NodeData: INTEGER
    # PRIVATE LeftNode: Node
    # PRIVATE RightNode: Node
    def __init__(self, data):
        self.__NodeData = data
        self.__LeftNode = None
        self.__RightNode = None

    #(ii)
    def GetData(self):
        return self.__NodeData
    def GetLeft(self):
        return self.__LeftNode
    def GetRight(self):
        return self.__RightNode

    #(iii)
    def SetLeft(self, left):
        self.__LeftNode = left
    def SetRight(self, right):
        self.__RightNode = right


# Part (b)
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)

#Part (c)
#(i)
class Tree:
    # PRIVATE FirstNode: Node
    def __init__(self, first_node):
        self.__FirstNode = first_node

    #(ii)
    def GetRootNode(self):
        return self.__FirstNode

    #(iii):
    def Insert(self,NewNode):
        CurrentNode = self.__FirstNode
        while True:
            if NewNode.GetData() < CurrentNode.GetData():
                #GO LEFT
                if CurrentNode.GetLeft() == None:
                    CurrentNode.SetLeft(NewNode)
                    return
                else:
                    CurrentNode = CurrentNode.GetLeft()
            else:
                #GO RIGHT
                if CurrentNode.GetRight() == None:
                    CurrentNode.SetRight(NewNode)
                    return
                else:
                    CurrentNode = CurrentNode.GetRight()

#Part (d):
def OutputInorder(ThisNode):
    if ThisNode != None:
        if ThisNode.GetLeft() != None:
            OutputInorder(ThisNode.GetLeft())
        print(ThisNode.GetData())
        if ThisNode.GetRight() != None:
            OutputInorder(ThisNode.GetRight())

#Part (e):
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)
MyTree = Tree(Node1)
MyTree.Insert(Node2)
MyTree.Insert(Node3)
MyTree.Insert(Node4)
MyTree.Insert(Node5)
OutputInorder(MyTree.GetRootNode())