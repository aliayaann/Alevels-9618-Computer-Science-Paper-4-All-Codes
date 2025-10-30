# ----------- Creating a Class ------------
class Vehicle:
    #PRIVATE ID: STRING
    #PRIVATE MaxSpeed: INTEGER
    #PRIVATE CurrentSpeed: INTEGER
    #PRIVATE IncreaseAmount: INTEGER
    #PRIVATE HorizontalPosition: INTEGER

# ------------- Constructors --------------
    def __init__(self, id, maxspe, incamo):         #Use Underscores to make Attributes Private
        self.__ID = id
        self.__MaxSpeed = maxspe
        self.__IncreaseAmount = incamo

        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    # -------------- Getters --------------
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    # -------------- Setters --------------
    def SetCurrentSpeed(self, NewCurrentSpeed):
        self.__CurrentSpeed = NewCurrentSpeed

    def SetHorizontalPosition(self, NewHorizontalPosition):
        self.__HorizontalPosition = NewHorizontalPosition

    # Creating a Method to Update CurrentSpeed with given value
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed


    # ------------------- Outputting Method -------------------
    def OutPutProcedure(self):
        print("Current Speed:",self.__CurrentSpeed)
        print("Current Horizontal Position:",self.__HorizontalPosition)

# -------------------------- INHERITANCE --------------------------
class Helicopter(Vehicle):
    #PRIVATE VerticalPosition: INTEGER
    #PRIVATE VerticalChange: INTEGER
    #PRIVATE MaxHeight: INTEGER

    def __init__(self, id, maxspe, incamo, verchan, maxhei):
        super().__init__(id, maxspe, incamo)
        self.__VerticalChange = verchan
        self.__MaxHeight = maxhei

        self.__VerticalPosition = 0

    # ----------------- Increase Speed Method -----------------
    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()

    # -------------- Child Class's Getters --------------------
    def GetVerticalPosition(self):
        return self.__VerticalPosition

    # ------------------- Outputting Method -------------------
    def OutPutProcedure(self):
        super().OutPutProcedure()
        print("Current Vertical Position:",self.__VerticalPosition)

# ------------------------ Main Program ------------------------

# --------------------- Creating Objects -----------------------
Car = Vehicle('Tiger',100,20)
Copter = Helicopter('Lion',350,40, 3, 100)

# ------------ Increasing Speed of Helicopter & Car ------------
Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutPutProcedure()

Copter.IncreaseSpeed()
Copter.IncreaseSpeed()
Copter.OutPutProcedure()