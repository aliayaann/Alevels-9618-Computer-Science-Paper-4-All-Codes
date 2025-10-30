# Part (a)
# Queue has 20 spaces
QueueData = ["" for _ in range(20)]
StartPointer = 0   # index of first element
EndPointer = -1    # index of last element
NumberOfItems = 0  # count of items in queue


# Part (b) Enqueue
def Enqueue(Item2Add):
    global QueueData, StartPointer, EndPointer, NumberOfItems
    if NumberOfItems == len(QueueData):   # queue full
        return False
    else:
        EndPointer = (EndPointer + 1) % len(QueueData)  # wrap around
        QueueData[EndPointer] = Item2Add
        NumberOfItems += 1
        return True


# Part (c) ReadFile
def ReadFile():
    global QueueData, StartPointer, EndPointer, NumberOfItems
    filename = input("Please enter a file name: ").strip()
    if filename == "DataToAdd.txt":
        path = r"C:\Users\aliay\Desktop\Text Files\DataToAdd.txt"
    elif filename == "SecondData.txt":
        path = r"C:\Users\aliay\Desktop\Text Files\SecondData.txt"
    else:
        return -1  # invalid file

    with open(path, "r") as f:
        for line in f:
            item = line.strip()
            if not Enqueue(item):  # if queue full
                return 1
        return 2  # success, all lines added


# Part (d)(i) Main program
filereading = ReadFile()
if filereading == -1:
    print("Sorry but the File couldn't be found")
elif filereading == 1:
    print("Sorry but the Queue is full")
else:
    print("Elements added successfully")


# Part (e) Remove
def Remove():
    global QueueData, StartPointer, EndPointer, NumberOfItems
    if NumberOfItems < 2:
        return "No Items"
    else:
        temp1 = QueueData[StartPointer]
        StartPointer = (StartPointer + 1) % len(QueueData)
        temp2 = QueueData[StartPointer]
        StartPointer = (StartPointer + 1) % len(QueueData)
        NumberOfItems -= 2
        return temp1 + " " + temp2
