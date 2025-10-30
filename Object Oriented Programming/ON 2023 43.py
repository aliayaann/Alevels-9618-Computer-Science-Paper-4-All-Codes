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
        self.SetIntelligence(self.__Intelligence*1.1)

    def ReturnAge(self):
        return 2023 - self.__DateofBirth.year


# ----------------------------------- Main Program -----------------------------------

#Normal Character:
FirstCharacter = Character('Royal',datetime.date(2019,1,1),70,30)
FirstCharacter.Learn()
print("The Character", FirstCharacter.GetName(), "is aged",FirstCharacter.ReturnAge(), "& has an Intelligence of",FirstCharacter.GetIntelligence())


# ------------------------------------- Sub-Class -------------------------------------
class MagicCharacter(Character):
    #PRIVATE Element: STRING
    def __init__(self, name, dob, intel, spee, elem):
        super().__init__(name, dob, intel, spee)
        self.__Element = elem

    def Learn(self):
        CurrentIntelligence = self.GetIntelligence()

        if self.__Element == 'fire' or self.__Element == 'water':
            self.SetIntelligence(CurrentIntelligence*1.2)
        elif self.__Element == 'earth':
            self.SetIntelligence(CurrentIntelligence*1.3)
        else:
            self.SetIntelligence(CurrentIntelligence*1.1)


FirstMagic = MagicCharacter('Light',datetime.date(2018,3,3),75,22, 'fire')
FirstMagic.Learn()
print("The Character", FirstMagic.GetName(), "is aged",FirstMagic.ReturnAge(), "& has an Intelligence of",FirstMagic.GetIntelligence())