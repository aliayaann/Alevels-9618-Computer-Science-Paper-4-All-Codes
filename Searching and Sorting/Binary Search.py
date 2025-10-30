arr=[1,2,3,4,5,6,7,8,9,10]
number2search=int(input("enter number you want to search inside the array: "))
def binarysearchalgo(arr,number2search):
    upperbound = len(arr)-1
    lowerbound = 0
    while lowerbound<=upperbound:
        midpoint=int((upperbound+lowerbound)/2)
        if arr[midpoint]==number2search:
            return midpoint
        elif number2search>arr[midpoint]:
            lowerbound=midpoint+1
        else:
            upperbound=midpoint-1
    return -1

result = binarysearchalgo(arr, number2search)
if result != -1:
    print("the number was found at the index",result)
else:
    print("lora khale")
