#Part a) (i):
class Employee:
    #PRIVATE HourlyPay: REAL
    #PRIVATE EmployeeNumber: STRING
    #PRIVATE JobTitle: STRING
    #PRIVATE PayYear2022: ARRAY[0:51] OF REAL
    def __init__(self, hourpay, employeeno, job,):
        self.__HourlyPay = hourpay
        self.__EmployeeNumber = employeeno
        self.__JobTitle = job
        self.__PayYear2022 = [0.0 for x in range(52)]

    #(ii)
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    #(iii)
    def SetPay(self, week, hoursworked):
        self.__PayYear2022[week] = hoursworked * self.__HourlyPay

    #(iv)
    def GetTotalPay(self):
        total = 0
        for x in range(len(self.__PayYear2022)):
            total = total + self.__PayYear2022[x]
        return total

# Part b) (i):
class Manager(Employee):
    #PRIVATE BonusValue: REAL
    def __init__(self, hourpay, employeeno, job, bonus):
        super().__init__(hourpay, employeeno, job,)
        self.__BonusValue = bonus

    #part (ii)
    def SetPay(self, week, hoursworked):
        hoursworked = hoursworked * (1 + (self.__BonusValue/100))
        super().SetPay(week, hoursworked)

#Part c)
EmployeeArray = []

pay = 0.00
ID = ""
Bonus = 0.00
Title = ""
Temp = ""
with open(r"C:\Users\aliay\Desktop\Text Files\Employees.txt","r") as f:
    while True:
        pay_line = f.readline()
        if not pay_line:  # end of file
            break
        pay = float(pay_line.strip())
        ID = f.readline().strip()
        next_line = f.readline().strip()

        # check if next line is a bonus (float) or a job title
        try:
            Bonus = float(next_line)
            Title = f.readline().strip()
            EmployeeArray.append(Manager(pay, ID, Title, Bonus))
        except ValueError:
            Title = next_line
            EmployeeArray.append(Employee(pay, ID, Title))


def EnterHours():
    with open(r"C:\Users\aliay\Desktop\Text Files\HoursWeek1.txt","r") as f:
        empid = ""
        for x in range(0,8):
            empid = f.readline().strip()
            for y in range(0,8):
                if EmployeeArray[y].GetEmployeeNumber() == empid:
                    EmployeeArray[y].SetPay(1, float(f.readline()))

EnterHours()
for x in range(0,8):
    print(EmployeeArray[x].GetEmployeeNumber(), "", EmployeeArray[x].GetTotalPay())