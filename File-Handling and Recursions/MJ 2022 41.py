global PlayerNames,PlayerScores

PlayerNames = []
PlayerScores = []
PreservedNames = []
PreservedScores = []

def ReadFiles():
    global PlayerNames, PlayerScores
    with open(r"C:\Users\aliay\Desktop\Text Files\HighScore.txt", "r") as f:
        while True:
            name = f.readline().strip()
            score = f.readline().strip()
            if not name or not score:
                break
            PlayerNames.append(name)
            PlayerScores.append(int(score))

def OutputScores():
    for x in range(len(PlayerNames)):
        print(PlayerNames[x], PlayerScores[x])

# ---------------------- Main Program ----------------------
ReadFiles()

#Preserve the Current State of the Arrays
PreservedNames = PlayerNames.copy()
PreservedScores = PlayerScores.copy()

OutputScores()

InputtedName = input("Please enter a Name: ")
while not (len(InputtedName)== 3) or InputtedName.isupper() or InputtedName.isalpha():
    PlayerName = input("Please enter a 3-Letter Name using only Capital Letters: ")
InputtedScore = int(input("Please enter a Score: "))
while InputtedScore < 1 or InputtedScore > 100000:
    InputtedScore = int(input("Invalid Score!, Please enter a score between 1 and 100000: "))

def InputScore(InputtedScore, InputtedName):
    global PlayerNames, PlayerScores
    PlayerNames.append(InputtedName)
    PlayerScores.append(InputtedScore)

    for x in (range(len(PlayerScores)-2, -1, -1)):
        if PlayerScores[x] < PlayerScores[x+  1]:
            PlayerScores[x], PlayerScores[x+1] = PlayerScores[x+1], PlayerScores[x]
            PlayerNames[x], PlayerNames[x+1] = PlayerNames[x+1], PlayerNames[x]

InputScore(InputtedScore, InputtedName)

print("Previously, the Leaderboard was:")
print("=================================")
for x in range(len(PreservedNames)):
    print(PreservedNames[x], PreservedScores[x])
print("=================================\n")
print("Now, the Leaderboard is:")
print("=================================")
OutputScores()

def WriteTopTen():
    global PlayerNames, PlayerScores
    with open(r"C:\Users\aliay\Desktop\Text Files\NewHighScore.txt", "w") as f:
        for index in range(10):
            f.write(PlayerNames[index] + "\n")
            f.write(str(PlayerScores[index]) + "\n")

WriteTopTen()