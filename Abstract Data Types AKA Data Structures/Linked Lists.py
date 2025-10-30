# ----------------------------- Linked List -----------------------------
# Setup:
Data = ["empty" for _ in range(10)]
Pointers = ["empty" for _ in range(10)]
NullPointer = -1
StartPointer = -1
NextFreePointer = 0

for x in range(len(Pointers)-1):
    Pointers[x] = x+1
Pointers[9] = NullPointer

def PrintingAlgo():
    global Data, Pointers, NullPointer, StartPointer
    for x in range(len(Data)):
        print(x,"-",Data[x],"-",Pointers[x])
    print("StartPointer:",StartPointer)
    print("NullPointer:",NullPointer)
print("Intial Linked List: ")
PrintingAlgo()
print("    -----    ")


#Adding an Element to the Linked List:
Amount2Add=int(input("Please enter an Amount to be added: "))
while Amount2Add<0 or Amount2Add>10:
    Amount2Add=int(input("Please enter an Amount b/w 0 and 10: "))
for x in range(Amount2Add):
    Number2Add = int(input("Please enter a Number to Add: "))
    if NextFreePointer == NullPointer:
        print("Sorry, the Linked List is full :(")
    else:
        Pointer2Number=StartPointer
        StartPointer=NextFreePointer
        NextFreePointer=Pointers[NextFreePointer]
        Data[StartPointer]=Number2Add
        Pointers[StartPointer]=Pointer2Number
print("    -----    ")
print("After Adding Elements: ")
PrintingAlgo()


#Searching the Linked List:
Value2Search = int(input("Please enter an Element to search: "))
Index=StartPointer
Found=False
while Index!=NullPointer and Found==False:
    if Data[Index]==Value2Search:
        Found=True
    else:
        Index=Pointers[Index]
if Found==True:
    print("    -----    ")
    print("Element Found @ index:",Index)
else:
    print("    -----    ")
    print("Not found :/")


#Deleting a Node in the Linked List:
Element2Delete = int(input("Please enter an Element to delete: "))
if StartPointer==NullPointer:
    print("Sorry, the Linked List is already empty :(")
else:
    Index = StartPointer
    OldIndex = Index
    Found = False
    while Index!=NullPointer and Found==False:
        if Data[Index] == Element2Delete:
            Found = True
        else:
            OldIndex = Index
            Index = Pointers[Index]
    if not Found:
        print("the number does not exist inside the Linked List")
    else:
        if Index==StartPointer: #The Element 2 Delete is @ 1st Index
            StartPointer=Pointers[Index]
        else:
            Pointers[OldIndex]=Pointers[Index]
        Data[Index]="empty"
        Pointers[Index]=NextFreePointer
        NextFreePointer=Pointers[NextFreePointer]
print("    -----    ")
print("After Deleting Elements: ")
PrintingAlgo()