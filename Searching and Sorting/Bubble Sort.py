#Bubble Sort
arr = [42, 7, 89, 13, 56, 24, 68, 3, 91, 35]

print(sorted(arr))

top = len(arr) - 1
for x in range(len(arr)):
    swap = False
    for i in range(top):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            swap = True
    if not swap:
        break

print(arr)


