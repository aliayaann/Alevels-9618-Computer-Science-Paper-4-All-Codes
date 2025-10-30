# --------- Question.1 ---------
#Part (a)
Stack = ["-1" for _ in range(20)]
TopOfStack = -1

#Part (b)
def Push(String2Add):
    global Stack, TopOfStack
    if TopOfStack == 19:
        return -1
    else:
        TopOfStack += 1
        Stack[TopOfStack] = String2Add
        return 1

#Part (c)
def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return '-1'
    else:
        temp = Stack[TopOfStack]
        Stack[TopOfStack] = "-1"
        TopOfStack -= 1
        return temp

#Part (d)
def ReadData(FileName):
    global Stack, TopOfStack
    try:
        with open(rf"C:\\Users\\aliay\\Desktop\\Text Files\\9618_s25_sf_42\\{FileName}", 'r') as f:
            for line in f:
                if Push(line.strip()) == -1:
                    print("Stack Full")
                    return
    except FileNotFoundError:
        print("File Not Found")

#Part (e)
def Calculate():
    global Stack, TopOfStack
    total = int(Stack[0])
    index = 1
    while index <= TopOfStack:
        Operator = Stack[index]
        Number = int(Stack[index+1])
        if Operator == "+":
            total = total + Number
        elif Operator == "-":
            total = total - Number
        elif Operator == "*":
            total = total * Number
        elif Operator == "/":
            total = total / Number
        elif Operator == "^":
            total = total ** Number
        index = index + 2
    return total

#Part (f)
UserInputFileName = input("Enter file name: ")
ReadData(UserInputFileName)
Result = Calculate()
print(Stack)
print(f"Total is,{Result}")


# --------- Question.2 ---------
#Part (a)
class NewRecord:
    def __init__(self,key,item1,item2):
        self.Key = key
        self.Item1 = item1
        self.Item2 = item2

#Part (b)
#(i)
Hashtable = ["" for _ in range(200)]
Spare = ["" for _ in range(100)]

#(ii)
def Initalize():
    for x in range(200):
        Hashtable[x] = NewRecord(-1,-1,-1)
    for x in range(100):
        Spare[x] = NewRecord(-1,-1,-1)

#Part (c)
def CalculateHash(key):
    Hash = int(key) % 200
    return Hash

#Part (d)
def InsertIntoHash(record):
    key2use = CalculateHash(record.Key)
    if Hashtable[key2use].Key == -1:
        Hashtable[key2use] = record
    else:
        index = 0
        while Spare[index].Key != -1:
           index += 1
        Spare[index] = record

#Part (e)
def CreateHashTable():
    try:
        with open(r"C:\\Users\\aliay\\Desktop\\Text Files\\9618_s25_sf_42\\HashData.txt",'r') as File:
            for line in File:
                parts = line.strip().split(",")
                key = parts[0]
                item1 = parts[1]
                item2 = parts[2]
                record = NewRecord(key,item1,item2)
                InsertIntoHash(record)
    except FileNotFoundError:
        print("File not found.")

#Part (f)
#(i)
def PrintSpare():
    for index in range(100):
        if Spare[index].Key != -1:
            print(Spare[index].Key)

#(ii)
Initalize()
CreateHashTable()
PrintSpare()


# --------- Question.3 ---------
#Part (a)
#(i)
class Animal:
    #PRIVATE Name, Sound: STRING
    #PRIVATE Size, Intelligence: INTEGER
    def __init__(self, name, sound, size, intel):
        self.Name = name
        self.Sound = sound
        self.Size = size
        self.Intelligence = intel

    #(ii)
    def Description(self):
        return f'The Animals name is {self.Name}, It makes a {self.Sound}, Its size is {self.Size} and its intelligence level is {self.Intelligence}.'

#Part (b)
#(i)
class Parrot(Animal):
    def __init__(self, name, sound, size, intelligence, wingspan, nowords):
        super().__init__(name, sound, size, intelligence)
        self.Wingspan = wingspan
        self.NumberWords = nowords

    def ChangeNumberWords(self,Change):
        self.NumberWords = self.NumberWords + Change

    #(ii)
    def Description(self):
        return f'The Animals name is {self.Name}, It makes a {self.Sound}, Its size is {self.Size} and its intelligence level is {self.Intelligence}. It has a wingspan of {self.Wingspan}cm and can say {self.NumberWords} of words.'

#Part (c)
#(i)
class Wolf(Animal):
    def __init__(self, name, sound, size, intelligence, tsize):
        super().__init__(name, sound, size, intelligence)
        self.TerritorySize = tsize

    def SetTerriorSize(self, ChangeinTSize):
        self.TerritorySize = self.TerritorySize + ChangeinTSize

    #(ii)
    def Description(self):
        return f'The Animals name is {self.Name}, It makes a {self.Sound}, Its size is {self.Size} and its intelligence level is {self.Intelligence}. It territory is {self.TerritorySize} square miles.'


#Part (d)
#(i)
parrot = Parrot('Chewie','Squawk',1,10,30,29)
wolf = Wolf('Nighteyes','Howl',8,7,100)
horse = Animal('Copper','Neigh',10,6)

#(ii)
wolf.SetTerriorSize(-20)
parrot.ChangeNumberWords(2)

print(wolf.Description())
print(parrot.Description())
print(horse.Description())