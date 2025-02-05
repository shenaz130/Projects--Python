class FooCooperation:
    def __init__ (self,name,bpay,hour):
        self.name = name
        self.bpay =bpay
        self.hour= hour

    def Salary(self,name,bpay,hour):
        if bpay >= 8:
            if hour <= 40:
                salary = bpay * hour
                print(name,"'s Salary is :",salary)
            elif hour >60:
                print("You can't work 60 hours!")
            else:
                hour = hour - 40
                salary= salary = bpay * hour *1.5
                print(name,"'s Salary is :",salary)
        else:
            print("base pay must not be lesser than minimum wage $8!")



fc1 = FooCooperation("emp1",9,30)

fc1.Salary("emp1",7.50,35)
fc1.Salary("emp2",8.20,47)
fc1.Salary("emp3",10,73)

