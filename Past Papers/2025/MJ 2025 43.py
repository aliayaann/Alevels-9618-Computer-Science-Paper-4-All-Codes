# --------- Question.1 ---------
#Part (a)
Queue = [-1 for _ in range(50)]
HeadPointer = -1
TailPointer = -1

#Part (b)
def Enqueue(Int2Store):
    global Queue, HeadPointer, TailPointer
    if TailPointer == 49:
        return False
    else:
        if HeadPointer == -1:
            HeadPointer = 0
        TailPointer = TailPointer + 1
        Queue[TailPointer] = Int2Store
        return True

#Part (c)
def Dequeue():
    global Queue, HeadPointer, TailPointer
    if TailPointer == -1:
        return -1
    else:
        Queue[TailPointer] = -1
        TailPointer = TailPointer - 1
        return Queue[TailPointer]

#Part (d)
def CreateQueue():
    global Queue, HeadPointer, TailPointer
    try:
        with open(r"C:\\Users\\aliay\\Desktop\\Text Files\\9618_s25_sf_43\\QueueData.txt",'r') as file:
            for line in file:
                if not Enqueue(int(line.strip())):
                    print("Queue full")
    except FileNotFoundError:
        print("Queue file not found")

#Part (e)
#(i)
CreateQueue()
total = 0
for Element in Queue:
    total = total + Dequeue()
print(total)


# --------- Question.2 ---------
#Part (a)
DataArray = [0,3,4,56,67,44,43,32,31,345,45,6,54,1]

#Part (b)
def InsertionSort(Array2Sort):
    lowerbound = 0
    upperbound = len(Array2Sort)-1
    for x in range(lowerbound+1, upperbound+1):
        Place = x-1
        Key = Array2Sort[x]
        while Place >= lowerbound and Array2Sort[Place] > Key:
            Temp = Array2Sort[Place+1]
            Array2Sort[Place+1] = Array2Sort[Place]
            Array2Sort[Place] = Temp
            Place -= 1
    return(Array2Sort)

#Part (c)
def OutputArray(Array2Print):
    String = ""
    index = 0
    while index < len(Array2Print):
        String = String + str(Array2Print[index]) + " "
        index = index + 1
    print(String.strip())

#Part (d)
#(i)
print('Before Sorting:')
OutputArray(DataArray)
print('   --------  ')
print('After Sorting:')
OutputArray(InsertionSort(DataArray))

def Search(ItemToFind, DataArray):
    upperbound = len(DataArray)-1
    lowerbound = 0
    while lowerbound <= upperbound:
        midpoint = lowerbound+(upperbound-lowerbound)//2
        if DataArray[midpoint] == ItemToFind:
            return midpoint
        elif DataArray[midpoint] < ItemToFind:
            lowerbound = midpoint+1
        else:
            upperbound = midpoint-1
    return -1

if Search(0, DataArray) == -1:
    print('Not Found')
else:
    print('Found @', Search(0, DataArray))
if Search(345, DataArray) == -1:
    print('Not Found')
else:
    print('Found @', Search(345, DataArray))
if Search(67, DataArray) == -1:
    print('Not Found')
else:
    print('Found @', Search(67, DataArray))
if Search(2, DataArray) == -1:
    print('Not Found')
else:
    print('Found @', Search(2,DataArray))


# --------- Question.3 ---------
#Part (a)
#(i)
class Node:
    #PRIVATE TheData: INTEGER
    #PRIVATE NextNode: Node
    def __init__(self,data,nextnode):
        self.__TheData=data
        self.__NextNode=nextnode

    #(ii)
    def GetData(self):
        return self.__TheData
    def GetNextNode(self):
        return self.__NextNode

    #(iii)
    def SetNextNode(self,node2add):
        self.__NextNode=node2add

#Part (b)
#(i)
class LinkedList:
    def __init__(self,head):
        self.__HeadNode=head

    #(ii)
    def InsertNode(self,Value2Add):
        NewNode = Node(Value2Add,-1)
        NewNode.SetNextNode(self.__HeadNode)
        self.__HeadNode=NewNode

    #(iii)
    def Traverse(self):
        string = ''
        CurrentNode=self.__HeadNode
        while CurrentNode != -1 and CurrentNode is not None:
            string = string + str(CurrentNode.GetData()) + ' '
            CurrentNode = CurrentNode.GetNextNode()
        return string.strip()

    def RemoveNode(self,Value2Remove):
        currentNode=self.__HeadNode
        previousNode = None

        while currentNode != -1 and currentNode is not None:
            if currentNode.GetData()==Value2Remove:
                if previousNode is None:
                    self.__HeadNode = currentNode.GetNextNode()
                else:
                    previousNode.SetNextNode(currentNode.GetNextNode())
                return True
            else:
                previousNode = currentNode
                currentNode = currentNode.GetNextNode()
        return False

Node5 = Node(50,None)
Node4 = Node(40,Node5)
Node3 = Node(30,Node4)
Node2 = Node(20,Node3)
Node1 = Node(10,Node2)
NewLinkedList = LinkedList(Node1)
print(NewLinkedList.Traverse())
print(NewLinkedList.RemoveNode(30))
print(NewLinkedList.Traverse())
