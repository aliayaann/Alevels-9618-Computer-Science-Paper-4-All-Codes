row = 5
column = 3

data = [[None for _ in range(column)]for _ in range(row)]
for x in range(row):
    data[x][0] = input("Please enter your name: ")
    data[x][1] = input("Please enter your email: ")
    data[x][2] = input("Please enter your password: ")


#to print in like excel jaisa
for i in range(row):
    print(data[i])

found = False
index = 0
while found == False and index < 2:
    if data[index][2] == "AnushayN":
        found = True
    else:
        index = index + 1

if found == True:
    print("found at: ",index)
else:
    print("not found")
