def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)

    for x in range(LengthString):
        FirstChar = Value[0]
        if FirstChar == 'a' or FirstChar == 'e' or FirstChar == 'i' or FirstChar == 'o' or FirstChar == 'u':
            Total = Total + 1
        Value = Value[1:len(Value)]
    return Total

temp = IterativeVowels('house')
print(temp)

def RecursiveVowels(Value):
    if len(Value) == 1:
        return 0
    else:
        FirstChar = Value[0]
        if FirstChar == 'a' or FirstChar == 'i' or FirstChar == 'o' or FirstChar == 'u' or FirstChar == 'e':
            Value = Value[1:len(Value)]
            return 1 + RecursiveVowels(Value)
        else:
            Value = Value[1:len(Value)]
            return RecursiveVowels(Value)

