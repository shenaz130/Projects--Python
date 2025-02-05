class Company:
    def __init__ (self):
        self.name = []
        self.idlist = []
        self.salary = []
        self.current = 0
        
    def SearchIndexById(self,id):
        for x in range (len(self.idlist)):
            if id == self.idlist[x]:
                print("index is = ",x, "Id is ", self.idlist[x])
                return x
                
        return -1
        
    def AddNewEmployee(self,name,id,salary):
        index = self.SearchIndexById (id)
        count = self.current +1
        if index == -1:
            if count <= 5:
                self.name.append(name)
                self.idlist.append(id)
                self.salary.append(salary)
                self.current = self.current +1
                print("New Employee", name, "Added.","Current is =",self.current)
            else:
                print("You exceeded the Array limit")
        else:
            print ("This Employee already Exist!!")
            
    def FindMaxSalary(self):
        max = self.salary[0]
        for x in range (len(self.salary)):
            if max < self.salary[x]:
                max =self.salary[x]
                print (self.salary[x], "is the highest salary taking by ", self.name [x])
                
    def FindMinSalary(self):
        min = self.salary[0]
        for x in range (len(self.salary)):
            if min > self.salary[x]:
                min == self.salary[x]
                print (self.salary[x], "is the lowest salary taking by ", self.name [x])

    def CalculateTotalSalary(self):
        for x in range (len(self.salary)):
            tot= sum(self.salary)
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

        
        
        
c1= Company ()
#print(c1.name)
#print(c1.SearchIndexById(1123))
print(c1.AddNewEmployee("Jane",1122,2345.90))
print(c1.AddNewEmployee("Ben",1123,1346.89))
print(c1.AddNewEmployee("Joe",1124,3450.20))
print(c1.AddNewEmployee("Frank",1125,1678.90))
print(c1.AddNewEmployee("Rome",1126,678.70))
print(c1.AddNewEmployee("Chan",1127,3278.90))
print(c1.SearchIndexById(1125))
print(c1.FindMaxSalary())
print(c1.FindMinSalary())
print(c1.CalculateTotalSalary())
print(c1.CalculateAverageSalary())
print(c1.PrintEmpData())




