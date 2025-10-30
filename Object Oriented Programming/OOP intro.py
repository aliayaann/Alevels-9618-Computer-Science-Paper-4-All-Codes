#      ╭───────────────────────────────╮
#      │         OOP — INTRO           │
#      ╰───────────────────────────────╯

# Class
#   ➝ A type that combines a data structure with
#      the methods that operate on it.

# Encapsulation
#   ➝ Combining data + subroutines into a class
#      and restricting external access to the data.

#  Methods
#   ➝ Subroutines inside a class.

# Attributes
#   ➝ Data items of a class (also called fields).

# Object
#   ➝ An instance of a class.

# Property
#   ➝ A class member that includes:
#         • Attribute (the data itself)
#         • Getter + Setter methods

#  Constructor
#   ➝ A special method called when creating a new object
#      to initialize its attributes.

# Getters (functions)
#   ➝ Used to *access* attribute values.

# Setters (procedures)
#   ➝ Used to *update* attribute values.


#      ╭─────────────────────────╮
#      │          EXTRA          │
#      ╰─────────────────────────╯

# • Classes have RECORDS → fields/attributes
# • Constructors initialize these fields
# • Methods (subroutines) update values

# Example:
#   In main program, we create an OBJECT of a class.
#   ▸ Send data → constructor
#   ▸ Constructor stores it in attributes
#   ▸ To read: use GETTERS
#   ▸ To update: use SETTERS

#  This entire mechanism is called ENCAPSULATION

# ================================== OOP INTRO ============================================
#Class: a type that combines a data structure with the methods that operate on the data structure
#Encapsulation: combining data and subroutines into a class and restricting external access to the data
#Methods: the subroutines of a class
#Attributes: the data items of a class (also sometimes referred to as fields)
#Object: an instance of a class
#Property: a class member that includes the attribute and also getter and setter method calls to access/set the attribute value
#Constructor: a ROUTINES
#2 types:-
# - Getters --> FUNCTIONS
# - Setters --> PROCEDspecial type of method that is called to create a new object and initialize its attributes
#Setter: a method to set the value of its associated attribute
#Getter: a method to access its associated attribute

#Classes has RECORDS -> which have fields/attributes
#Constructors are to INITIALIZE fields
#METHODS ARE SUBURES (used to update a value)

# ------------------------------------------------------------------------------------------
#We will make an "OBJECT" of Class in Main Program, Object will have access to Constructor
#EG we send the value Ayaan and Mercedes AMG PETRONAS in Class.
#The Constructor will initialize these Names in the records/attribues.
#TO ACCESS THESE RECORDS we use Getters, to update we use SETTERS
# ---------------------------- this shit is called ENCAPSULATION ----------------------------

class F1Drivers:
    def __init__(self,name,num,team):
        self.__Name = name         #We Use Underscores to make it Private
        self.__Number = num
        self.__RaceTeam = team
        self.__Sponser = team

    # ------- Getters -------
    def GetName(self):
        return self.__Name

    def GetNumber(self):
        return self.__Number

    def GetRaceTeam(self):
        return self.__RaceTeam

    # ------- Setters ------
    def SetRaceTeam(self,teamname):
       self.__RaceTeam = teamname

    def SetName(self,drivername):
        self.__Name = drivername

    def SetNumber(self,drivernum):
        self.__Number = drivernum


# ------- All this is Private, the user CAN NOT ACCESS THIS SHIT AT ALL -------
# this is why we use Getters/Setters because the Records are PRIVATE

SFD1 = F1Drivers('',0,'')

print("Welcome! to the FORMULA ONE, New Team Creator:")
teamname = input("What is your team name? ")
SFD1.SetRaceTeam(teamname)

drivername = input("What is your driver name? ")
SFD1.SetName(drivername)

drivernum = input("What is your driver's number? ")
SFD1.SetNumber(drivernum)

teamnameplaceholder = SFD1.GetRaceTeam()
drivernameplaceholder = SFD1.GetName()
drivernumplaceholder = SFD1.GetNumber()

print(f"{drivernameplaceholder} now drives for {teamnameplaceholder}, using the Number #{drivernumplaceholder}")