#Queues
#two pointers

arr = ["empty" for _ in range(10)]
frontpointer = 0
rearpointer = 0

def enqueue(data2add):
    global arr
    global frontpointer
    global rearpointer
    arr[rearpointer] = data2add
    return True

def dequeue():
    global arr
    global frontpointer
    temp = arr[frontpointer]
    arr[frontpointer] = "remove"
    return temp

# ------ main program ------
amount2add = int(input("Please enter the amount of the elements to add: "))
if amount2add < 0 or amount2add > 10:
    amount2add = int(input("Please enter a number between 0 and 10: "))
for x in range(amount2add):
    data2add = int(input("Please enter a number to add: "))
    if enqueue(data2add) == True:
        rearpointer += 1
        if rearpointer > 10:
            rearpointer = 0

for i in range(10):
    print(i,arr[i])
print("frontpointer:",frontpointer)
print("rearpointer:",rearpointer)

amount2remove = int(input("Please enter the amount of the elements to remove: "))
if amount2remove < 0 or amount2remove > 10:
    amount2remove = int(input("Please enter a number between 0 and 10: "))
for x in range(amount2remove):
    temp = dequeue()
    print("the number removed was",temp)
    frontpointer += 1
    if frontpointer > 10:
        frontpointer = 0

for i in range(10):
    print(i,arr[i])
print("frontpointer:",frontpointer)
print("rearpointer:",rearpointer)
