# Stacks
#part a)
StackData = [0 for _ in range(9)]
StackPointer = 0 #Points to the NEXT FREE SPACE

#part b)
def printing():
    global StackPointer, StackData
    for x in range(9):
        print(x, " - ", StackData[x])
    print("StackPointer: ",StackPointer)

#part c)
def push(integer):
    global StackPointer, StackData
    if StackPointer >= 9:
        return False
    else:
        StackData[StackPointer] = integer
        StackPointer += 1
        return True

#part d) i):
amount2add = int(input("How many elements would you like to add?: "))
for x in range(amount2add):
    elem2add = int(input("Please enter your element: "))
    result = push(elem2add)
    if result:
        print("the element was added successfully")
    else:
        print("the element was not added. Stack is full.")

#part e) i)
def pop():
    global StackPointer, StackData
    if StackPointer == 0:
        return -1
    else:
        StackPointer -= 1
        temp = StackData[StackPointer]
        StackData[StackPointer] = 0
        return temp

amount2remove = int(input("How many elements would you like to remove?: "))
for x in range(amount2remove):
    result2 = pop()
    if result2 == -1:
        print("the element was not removed. Stack is full.")
    else:
        print("the element,",result2,",was removed.")





