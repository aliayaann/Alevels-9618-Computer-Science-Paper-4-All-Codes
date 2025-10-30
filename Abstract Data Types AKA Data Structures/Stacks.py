# 2 Pointers
# Last in, First Out
Arr = ["empty" for _ in range(10)]
TopPointer = 0

#Push (removing an Element)
def push(Data2Add):
    global TopPointer
    global Arr
    if TopPointer >= 10:  # checking for overflow
        return False
    else:
        Arr[TopPointer] = Data2Add
        return True

#Popping (removing an Element)
def pop():
    global TopPointer
    global Arr
    if TopPointer < 0:
        return False
    else:
        Arr[TopPointer] = "empty"
        return True

# ----- Main Program -----

Amount2Add = int(input("Please enter the amount of elements to add to the stack: "))
while Amount2Add < 0 or Amount2Add > 10:
    Amount2Add = int(input("Please enter an amount between 0 and 10: "))
for x in range(Amount2Add):
    Data2Add = int(input("Please enter the a number to add to the stack: "))
    if push(Data2Add) == True:
        print("Number added successfully!.")
        TopPointer += 1
    else:
        print("Number not added. Stack overflow!")

#Printing the Stack
for i in reversed(range(10)):
    print(i, Arr[i])
print("Top Pointer:",TopPointer)

Amount2Remove = int(input("Please enter the amount of elements to remove from the stack: "))
while Amount2Remove < 0 or Amount2Remove > 10:
    Amount2Remove = int(input("Please enter an amount between 0 and 10: "))
for x in range(Amount2Remove):
    result = pop()
    if result == True:
        print("Number removed successfully!.")
        TopPointer -= 1
    else:
        print("Number not removed. Stack is already empty!")

#Printing the Stack
for i in reversed(range(10)):
    print(i, Arr[i])
print("Top Pointer:",TopPointer)