#Linear Search
#part a)
arrayData = [10,5,6,7,1,12,13,15,21,8]

#part  b)
#i)
def LinearSearch(Element2Find):
    for index in range(len(arrayData)):
        if arrayData[index] == Element2Find:
            return True
    return False
UserValue = int(input("Please enter a value to search: "))
if LinearSearch(UserValue):
    print("The Value exists in the Array")
else:
    print("The Value doesn't exist in the Array")