#expr = "76 + 549 - 94349 * 93843 / 9437"
#result = eval(expr)
#print(f"The result of '{expr}' is: {result}")

#If your file contains a math expression vertically or diagonally, like:
#232
#+
#232323
#-
#232
#*
#2323
#^
#23

#And you want to evaluate it as a proper math expression, here's how you can do it step-by-step.
#Step-by-step Plan:
# - Read the lines from the file.
# - Clean and join them into a single string expression.
# - Handle operators like ^ (which in Python means bitwise XOR, but usually means exponentiation **).
# - Evaluate the expression safely

#expr = "".join(lines)  # Join all lines into one expression
# Replace ^ with ** to make it valid Python exponentiation
#expr = expr.replace("^", "**")
# Evaluate the expression safely
#result = eval(expr)
#print(f"The result of the expression is: {result}")

import datetime


class Character:
    #PRIVATE CharacterName: STRING
    #PRIVATE DateofBirth: DATE
    #PRIVATE Intelligence: REAL
    #PRIVATE Speed: INTEGER
    def __init__(self, name, dob, intel, spee):
        self.__CharacterName = name
        self.__DateofBirth = dob
        self.__Intelligence = intel
        self.__Speed = spee

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self, IntelligenceValue):
        self.__Intelligence = IntelligenceValue

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1

    def ReturnAge(self):
        return 2023 - self.__DateofBirth.year

# ------------------ Main Program ------------------
FirstCharacter = Character('Royal',datetime.date(2019,1,1),70,30)
FirstCharacter.Learn()
charname = FirstCharacter.GetName()
charage = FirstCharacter.ReturnAge()
charintel = FirstCharacter.GetIntelligence()
print("After Learning:")
print("The Character", charname, "is aged",charage, "& has an Intelligence of",charintel)

class MagicCharacter(Character):
    #PRIVATE Element: STRING
    def __init__(self, name, dob, intel, spee, elem):
        super().__init__(name, dob, intel, spee)
        self.__Element = elem

    def Learn(self,magicintel):
        if self.__Element == 'fire' or self._Element == 'water':
            magicintel = magicintel*1.2
        if self._Element == 'earth':
            magicintel = magicintel*1.3
        else:
            magicintel = magicintel*1.1

    def ReturnMagicAge(self):
        super().ReturnAge()


FirstMagic = MagicCharacter('Light',datetime.date(2018,3,3),75,22, 'fire')
charname = FirstMagic.GetName()
charage = FirstMagic.ReturnAge()
magicintel = FirstMagic.GetIntelligence()
magicintel.Learn()
charintel = magicintel
print("After Learning:")
print("The Character", charname, "is aged",charage, "& has an Intelligence of",charintel)