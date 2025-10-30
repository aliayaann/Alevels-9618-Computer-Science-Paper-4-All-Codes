def IterativeCalculate(Number):
    ToFind = Number
    Total = 0
    while Number != 0:
        if ToFind % Number == 0:
            Total = Total + Number
        Number = Number - 1
    return Total
print("Iterative:",IterativeCalculate(50))

def RecursiveCalculate(Number,ToFind):
    if Number == 0:
        return 0
    else:
        if ToFind % Number == 0:
            return Number + RecursiveCalculate(Number-1, ToFind)
        else:
            return RecursiveCalculate(Number - 1, ToFind)
print("Recursive:",RecursiveCalculate(50,50))
