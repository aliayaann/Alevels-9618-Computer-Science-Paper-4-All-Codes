arr = [12,15,16,8,5,19]
lowerbound = 0
upperbound = len(arr)-1

for index in range(lowerbound+1, upperbound+1):
    place=index-1
    key=arr[index]
    if arr[place] > key:
        while place>=lowerbound and arr[place]>key:
            temp=arr[place+1]
            arr[place+1]=arr[place]
            arr[place]=temp
            place = place-1
print(arr)