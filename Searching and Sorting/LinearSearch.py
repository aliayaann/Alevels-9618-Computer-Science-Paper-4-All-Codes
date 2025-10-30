#Linear Searching
arr = [x+1 for x in range(10)]

Num2Search=int(input("gimme a number to search"))

def linearsearch(arr, Num2Search):
    for i in range(len(arr)):
        if  Num2Search == arr[i]:
            return i
    return -1

index = linearsearch(arr, Num2Search)

if index == -1:
    print("sadly, it is not in array :(")
else:
    print("the number you gave is in array WOOHOO :D at the index",index)
