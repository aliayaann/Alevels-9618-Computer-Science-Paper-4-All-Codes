#Part a)
class Cards:
    #PRIVATE Number: INTEGER
    #PRIVATE Color: STRING
    def __init__(self, no, col):
        self.__Number = no
        self.__Color = col

    #Part b)
    def GetNumber(self):
        return self.__Number

    def GetColor(self):
        return self.__Color

#Part c)
CardArray = []
with open(r"C:\Users\aliay\Desktop\Text Files\CardValues.txt","r") as file:
    for i in range(30):
        Num = int(file.readline().strip())
        Color = file.readline().strip()
        CardArray.append(Cards(Num,Color))

for x in range(30):
    print(CardArray[x].GetNumber(),  CardArray[x].GetColor())

#Part d)
CardChoosen = []
def ChooseCard():
    global CardChoosen, CardArray
    while True:
        cardselect = int(input("Please select a card (1–30): ")) - 1  # -1 for 0-based index
        if cardselect < 0 or cardselect >= 30:
            print("Invalid number. Must be between 1 and 30.")
        elif cardselect in CardChoosen:
            print("You already chose that card.")
        else:
            CardChoosen.append(cardselect)  # record index chosen
            return cardselect

#Part e)
Player1 = []
print("Player 1, please input your 4 cards")
for x in range(4):
    cardchoosenn = ChooseCard()
    Player1.append(CardArray[cardchoosenn])
for x in range(4):
    print(Player1[x].GetNumber(), Player1[x].GetColor())


