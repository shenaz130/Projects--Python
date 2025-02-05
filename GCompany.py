class Employee:
    def __init__ (self, name, rank, years,etype):
        self.name = name
        self.rank =rank
        self. years = years
        self.etype = etype
    

e1 = Employee ("John", 6, 4, "Employee")
e2 = Employee ("Jack", 4, 3, "Employee")
e3 = Employee ("Mel", 3, 7, "Employee")
e4 = Employee ("Joe", 4, 10, "Employee")

class Manager(Employee):
    def __init__(self, name, rank, years,noEmp,etype):
        Employee.__init__(self, name, rank, years,etype)
        self.noEmp = noEmp
 
m1 = Manager("Brad",2, 8,10, "manager")

class Consultant(Employee):
    def __init__(self, name, rank, years,hours,etype):
        Employee.__init__(self, name, rank, years, etype)
        self.hours = hours


con1 = Consultant("Mike",14, 7,40,"consultant")
con2 = Consultant("Jade",8, 5,35,"consultant")
con3 = Consultant("Chris",6, 8,20,"consultant")

class Company:
    employeelist = []
    def __init__ (self, name):
        self.name = name
        self.employeelist = []

    def addEmployee(self, aEmp):
        self.employeelist.append(aEmp)
        print("new employee added! ")
        #print(len(self.employeelist))

    def calculateSalary(self):
        for x in range (len(self.employeelist)):
            if self.employeelist[x].etype == "Employee" :
                Salary = [(self.employeelist[x].years * 500 )+ (self.employeelist[x].rank *1000)]
                print(self.employeelist[x].name,"'s Salary is =", Salary)
            elif self.employeelist[x].etype == "manager" :
                Salary = [(self.employeelist[x].years * 500 )+ (self.employeelist[x].rank *1500)+ (self.employeelist[x].noEmp *10)]
                print(self.employeelist[x].name,"Manager's Salary is =", Salary)
            elif self.employeelist[x].etype == "consultant" :
                Salary = [ (self.employeelist[x].hours *1000)+ (self.employeelist[x].rank *500)]
                print(self.employeelist[x].name,"Consultant's Salary is =", Salary)

    def Display(self):
        print("-----------------------------------------")
        print("Employee - Rank - Years of Exp. - Position")
        print("-----------------------------------------")
        for x in range (len(self.employeelist)):
            print(self.employeelist[x].name,"    -   ",self.employeelist[x].rank,"    -  ", self.employeelist[x].years, " -  ",self.employeelist[x].etype)
        print("------------------------------------------")
        

company1 = Company("Tech-New Company")
company1.addEmployee(e1)
company1.addEmployee(e2)
company1.addEmployee(e3)
company1.addEmployee(e4)
company1.addEmployee(m1)
company1.addEmployee(con1)
company1.addEmployee(con2)
company1.addEmployee(con3)
print("------------------------------------------")
print("Welcome to ",company1.name )
print("Employee Details >>>>")
company1.Display()
company1.calculateSalary()
