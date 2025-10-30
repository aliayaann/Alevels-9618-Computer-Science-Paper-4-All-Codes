# ------------------------- Binary Tree -------------------------
# Initalization:
class BinaryTree:
    def __init__(self,left,data,right):
        self.LeftPointers = left
        self.DataElem = data
        self.RightPointers = right
TreeArray = []
RootPointer = -1
NextFreePointer = 0
for x in range(5):
    Node = BinaryTree(x+1,"",0)
    TreeArray.append(Node)
LastNode = BinaryTree(-1,"",0)
TreeArray.insert(6,LastNode)

def printing():
    for x in range(6):
        print(x,"-",TreeArray[x].LeftPointers,"|",TreeArray[x].DataElem,"|",TreeArray[x].RightPointers)
print("    -----    ")
print("Initial Binary Tree: ")
printing()


#Preserve the value of NextFreePointer
#Update the value of NextFreePointer using the LeftPointer
#Add the data element, set the l`eft and right pointer as -1
#If root pointer is set to -1, set it to 0
# Adding Elements to the Binary Tree
Amount2Add = int(input("Enter the Amount of Elements to Add: "))
while Amount2Add < 0 or Amount2Add > len(TreeArray):
    Amount2Add = int(input("Enter an Amount Between O and 6: "))
for index in range(Amount2Add):
    Element2Add = int(input("Enter the Element to Add: "))
    if NextFreePointer == -1:
        print("Sorry the Binary Tree is full")
    else:
        NewNodePointer = NextFreePointer
        NextFreePointer = TreeArray[NewNodePointer].LeftPointers
        TreeArray[NewNodePointer].DataElem = Element2Add
        TreeArray[NewNodePointer].RightPointers = -1
        TreeArray[NewNodePointer].LeftPointers = -1
        if RootPointer == -1:
            RootPointer = NewNodePointer
        else:
            CurrentNodePointer = RootPointer
            while CurrentNodePointer != -1:
                PreviousNodePointer = CurrentNodePointer
                if TreeArray[CurrentNodePointer].DataElem > Element2Add:
                    TurnLeft = True
                    CurrentNodePointer = TreeArray[PreviousNodePointer].LeftPointers
                else:
                    TurnLeft = False
                    CurrentNodePointer = TreeArray[PreviousNodePointer].RightPointers
            if TurnLeft:
                TreeArray[PreviousNodePointer].LeftPointers = NewNodePointer
            else:
                TreeArray[PreviousNodePointer].RightPointers = NewNodePointer
print("    -----    ")
print("After Adding Elements: ")
printing()


#Searching an Element in Binary Tree:
Value2Search = int(input("Enter the Value to Search: "))
Index = RootPointer
while Index != -1 and TreeArray[Index].DataElem != Value2Search:
    if TreeArray[Index].DataElem > Value2Search:
        Index = TreeArray[Index].LeftPointers
    else:
        Index = TreeArray[Index].RightPointers
if Index == -1:
    print("    -----    ")
    print("Sorry the Number was not found in the Binary Tree")
else:
    print("    -----    ")
    print("Number was found @ index", Index)