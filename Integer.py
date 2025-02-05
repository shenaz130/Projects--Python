class MyInteger:
    def __init__(self):
        self.value = 0
        global i
        global i2
           
    
    def isEven(self):
        print("n1 is even?")
        if i % 2 == 0:
            print("True")
        else :
            print("False")

    def isPrime(self):
        print("n1 is Prime?")
        for n in range(2, i):
            x = "true"
            if i % n == 0:
                x= "false"
                break 
        return print(x)
 

    def isOdd(self):        
        print("n2 is Odd?")
        if (i2 % 2 != 0):
            print("True")
        else :
            print("False")
        
            
    def isEqual(self):
        print("n1 is Equal to n2?")
        if (i == i2):
            print("True", i, i2)
        else :
            print("False", i, i2)

        print("n1 is Equal to 5?")
        if i == 5:
            print("True")
        else :
            print("False")
            
    def add(self):
        print("n1 value after n1.add(n2)")
        print(i + i2)
    
    def sub(self):
        print("n1 value after n2.sub(n1)")
        print(i2 - i)
    
    def mul(self):
        print("n1 value after n1.mul(n2)")
        print(i * i2)

    def div(self):
        print("n2 value after n2.div(n1)")
        print(i2 / i)

   

myint = MyInteger()
i =(int(input("n1 value is : ")))

myint.isEven()
myint.isPrime()
i2 =(int(input("n2 value is : ")))
myint.isOdd()
myint.isEqual()
myint.add()
myint.sub()
myint.mul()
myint.div()






