# hardcoded tree (left, data, right)
ArrayNodes = [
    [1, 20, 5],   # index 0
    [2, 15, -1],  # index 1
    [-1, 3, 3],   # index 2
    [-1, 9, 4],   # index 3
    [-1, 10, -1], # index 4
    [-1, 58, -1], # index 5
    [-1, -1, -1]  # index 6
]

def SearchValue(Root, ValuetoFind):
    if Root == -1:
        return -1
    node_data = ArrayNodes[Root][1]
    if node_data == ValuetoFind:
        return Root
    elif ValuetoFind < node_data:
        return SearchValue(ArrayNodes[Root][0], ValuetoFind)
    else:
        return SearchValue(ArrayNodes[Root][2], ValuetoFind)

def PostOrder(Root):
    if Root == -1:
        return
    PostOrder(ArrayNodes[Root][0])  # left
    PostOrder(ArrayNodes[Root][2])  # right
    print(ArrayNodes[Root][1], end=" ")

for i in range(7):
    print(ArrayNodes[i])

value2find = int(input("Please enter the Number you Want to Find: "))  # e.g. 15
foundvalue = SearchValue(0, value2find)
if foundvalue == -1:
    print("Sorry, the value you entered was not found.")
else:
    print(f"The value, {value2find} was found at the index, {foundvalue}.")

print("\n------ POSTORDER: ------")
PostOrder(0)
print()
