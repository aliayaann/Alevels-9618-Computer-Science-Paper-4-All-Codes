#ON 2021 42
# for DIV --> print(int(13/2)) or print(13//2)

def Unknown(x,y):
    if x < y:
        print(x+y)
        return Unknown(x+1,y) * 2
    else:
        if x == y:
            return 1
        else:
            print(x+y)
            return int(Unknown(x-1,y)/2)


print(" ---------------- Recursive Cases ---------------- ")
print("Case 1:")
print("The Value of X is 10, while the value of Y is 15.")
print("Answer:")
print(Unknown(10,15),"\n")

print("Case 2:")
print("The Value of X is 10, while the value of Y is also 10.")
print("Answer:")
print(Unknown(10,10),"\n")

print("Case 3:")
print("The Value of X is 15, while the value of Y is 10.")
print("Answer:")
print(Unknown(15,10),"\n")

def UnknownIterative(x,y):
    result = 1
    while x != y:
        print(x+y)
        if x < y:
            x = x+1
            result = result*2
        else:
            x = x-1
            result = result//2
    return result

print(" ---------------- Iterative Cases ---------------- ")
print("Case 1:")
print("The Value of X is 10, while the value of Y is 15.")
print("Answer:")
print(UnknownIterative(10,15),"\n")

print("Case 2:")
print("The Value of X is 10, while the value of Y is also 10.")
print("Answer:")
print(UnknownIterative(10,10),"\n")

print("Case 3:")
print("The Value of X is 15, while the value of Y is 10.")
print("Answer:")
print(UnknownIterative(15,10),"\n")


