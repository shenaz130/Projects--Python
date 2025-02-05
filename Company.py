class Company:
    def __init__(self):
        self.idlist = []
        self.name = []
        self.salary=[]
        self.current = 0
    
    def SearchIndexById(self,id):
        for x in range (len(self.idlist)):
            if id == self.idlist[x]:
                print("index is = ",x, " and the Id is ", self.idlist[x])
                return x
                
        return -1

    def AddNewEmployee(self):
        index = self.SearchIndexById (id)
        count = self.current +1
        if index == -1:
            if count <= 5:
                nid = input("")
                name = input("")
                salary = input("")

                self.name.append(name)
                self.idlist.append(nid)
                self.salary.append(salary)
                self.current = self.current +1
                print("New Employee", name, "Added.","Current position is =",self.current)
            else:
                print("You exceeded the Array limit")
        else:
            print ("This Employee already Exist!!")
            
            
    def PrintEmpData (self):
        for x in range (len(self.idlist)):
            print ("---------------------------")
            print("Printing Employee data")
            print ("---------------------------")
            print ("Id : ",self.idlist[x])
            print ("Name : ",self.name[x])
            print ("Salary : ",self.salary[x])
            print ("---------------------------")
            
    def FindMaxSalary(self):
        max = self.salary[0]
        for x in range (len(self.salary)):
            if max < self.salary[x]:
                max =self.salary[x]
        print (max, "is the highest salary taking by ", self.name [x])
                
    def FindMinSalary(self):
        min = self.salary[0]
        for x in range (len(self.salary)):
            if min > self.salary[x]:
                min = self.salary[x]
        print (min, "is the lowest salary taking by ", self.name [x])

    def CalculateTotalSalary(self):
        tot= 0
        for x in range (len(self.salary)):
            tot = tot + self.salary[x]
        print ("Total Salary amount is = ", tot)
                

    def CalculateAverageSalary(self):
        tot =0
        count = 0
        for x in range(len(self.salary)):
            tot = tot + self.salary[x]
            count = count +1
        print("Average Salary amount is = ", tot/count)

    def PrintEmpData (self):
        for x in range (len(self.idlist)):
            print ("---------------------------")
            print("Printing Employee data")
            print ("---------------------------")
            print ("Id : ",self.idlist[x])
            print ("Name : ",self.name[x])
            print ("Salary : ",self.salary[x])
            print ("---------------------------")

        if len(self.idlist) ==0:
            print("No data to print")

 

  
c1 = Company()
def menu():
    print ("Welcome to the Company system")
    print ("1)Add a new Employee Info")
    print ("2)Quit")
    
    
i=1
while i ==1:
    menu()
    choice = int(input("Your choice?  "))
    if choice == 1:
        print("Enter your Employee ID, Name and Salary respectively")
        c1.AddNewEmployee()
        print("Employee Data were added Successfully")

    elif choice == 2:
        i=i+1
        c1.PrintEmpData()
        c1.FindMaxSalary()
        c1.FindMinSalary()
        c1.CalculateTotalSalary()
        c1.CalculateAverageSalary()
    else :
        print("invalid choice!!")
      
    
       

       
menu()
#c1.PrintEmpData()
#Company.addEmployee()
#Company.MaxSalary()




