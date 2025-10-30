#Binary Search question
#SHIT WAS VERY EASY :/

import random

array = [[random.randint(1,100) for _ in range(10)]for _ in range(10)]

#for x in range(10):
    #print(array[x])

for row in array:
    formatted_row = ", ".join(f"{val:2}" for val in row)  # :2 = align numbers
    print(f"[ {formatted_row} ]")
print(" ")

# Bubble Sort
ArrayLength = 10
for x in range(ArrayLength):
    for y in range(ArrayLength-1):
        for z in range(ArrayLength-y-1):
            if array[x][z] > array[x][z+1]:
                temp = array[x][z]
                array[x][z] = array[x][z+1]
                array[x][z+1] = temp
print(" ")
print(" ------------------ Bubble Sort ------------------")
for row in array:
    formatted_row = ", ".join(f"{val:2}" for val in row)  # :2 = align numbers
    print(f"[ {formatted_row} ]")
print(" ")
print(" ")

# Binary Search
def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + Upper) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    return -1
print(" ------------------ Binary Search ------------------")
Value2Search = 16
valuefoundindex = BinarySearch(array,0,9,Value2Search)
if valuefoundindex == -1:
    print("not found")
else:
    print("found at", valuefoundindex)
