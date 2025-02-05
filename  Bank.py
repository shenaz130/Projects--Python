class Bank:

    def __init__(self,name):
        self.name= name
        self.accNumlist=[]
        self.balance=[]
        self.type=[]
        self.current= 0
        
#searchIndexOfAccNumber(accNb : int ) : returns the index in array of the account number accNb, otherwise returns -1.
    def searchIndexOfAccNumber(self, accNb):
        for x in range(len(self.accNumlist)):
            if accNb==self.accNumlist[x]:
                return x
        
        return -1
            
    def deposit(self, accNb, amount):
        index = self.searchIndexOfAccNumber(accNb)
        self.balance[index] = self.balance[index] + amount

    def withdraw(self, accNb, amount):
        index = self.searchIndexOfAccNumber(accNb)
        self.balance[index] = self.balance[index] - amount
    
    def addNewAccount(self, accNb, amount ):
       
        index = self.searchIndexOfAccNumber(accNb)
       
        if index==-1 :
            self.accNumlist.append(accNb)
            self.balance.append(amount)
            if amount >= 2000: 
                self.type.append("SA")
            else :
                self.type.append("CH")
            self.current = self.current + 1
        else: 
            print("This account is already created!!!")
    
    def display(self, type):
        for x in range(self.current):
            if self.type[x] == type:
                print("Account#: ", self.accNumlist[x])
                print("Balance: ",  self.balance[x])
                print("Account type: ", self.type[x])
                print("=============================")

    def MaxBalance(self):
        #index = self.searchIndexOfAccNumber(accNb)
        max = self.balance[0]
        for x in range(len(self.balance)):
            if max < self.balance[x]:
                max = self.balance[x]
        print(max,self.accNumlist[x])


    def AvgBalance(self, type):
        count = 0
        tot = 0
        
        for x in range (len(self.balance)):
            if type == self.type[x]:
                tot = tot + self.balance[x]
                count = count +1
    
        print("Average = ", tot/count)

    """ avg = self.balance[0]
        avg = sum(self.balance)/(len(self.accNumlist))
        print(avg)"""
    
    def TotBalance(self):
        for x in range (len(self.balance)):
            tot = sum(self.balance)
        print("Total balance in the bank is = ", tot)
    
    def MaxType(self,type):
        max= 0

        for x in range (len(self.type)):
            if type == self.type[x]:
                max = max +1
                print(type,"has the Maximum Account Numbers =",max)

    def MinType(self,type):
        min= 0

        for x in range (len(self.type)):
            if type != self.type[x]:
                min = min +1
                print(type,"has the Minimum Account Numbers =",min)

    def DelType(self,type):
        for x in range (len(self.type)):
            if type == self.type[x]:
                self.type.remove(type)
                print(type,"Type has been Deleted")


b1=Bank("TD Bank")
print(b1.name)
b1.addNewAccount(1111,700)
b1.addNewAccount(1112,1700)
b1.addNewAccount(1113,7700)
b1.addNewAccount(1114,77700)
b1.display("SA")
b1.MaxBalance()
b1.AvgBalance("SA")
b1.TotBalance()
b1.MaxType("SA")
b1.addNewAccount(1115,300)
b1.MinType("CH")
b1.DelType("CH")

