class Resturant:
    def __init__(self,name,location,contact):
        self.name = name
        self.location = location
        self.contact = contact
        self.menulist= []
        self.dishlist = []
        self.dessertlist =[]
        self.lunchlist =[]

    menulist =[]
    def addMenu(self,aMenu):
        self.menulist.append(aMenu)
        print(len(self.menulist),aMenu.name,"Menu")

r1 = Resturant("Sage & Salt", "Toronto","416-234-5654")
class Menu:
    def __init__(self,name):
        self.name = name 

    lunchlist =[]
    dessertlist =[]
    dishlist = []
    def addDish (self,aDish):
        self.dishlist.append(aDish)
        print ("New dish Added to the menu!",aDish.name)

    def addDessert(self,aDessert):
        self.dessertlist.append(aDessert)
        print ("New dessert Added to the menu!",aDessert.name)
    
    def addLunch(self,alunch):
        self.lunchlist.append(alunch)
        print ("Timings Added")


    def displayMenu(self):
            print("Welcome to the Menu")
            print("item   -   price")
            print("-----------------------")
            for x in range (len(self.dishlist)):
                print(self.dishlist[x].name,"- $",self.dishlist[x].price)

            print("-----------------------")
            print("Dessert Menu")
            print("item   - type -   price")
            print("-----------------------")
            for x in range (len(self.dessertlist)):
                print(self.dessertlist[x].name,"-",self.dessertlist[x].dtype,"- $",self.dessertlist[x].price)

            print("-----------------------")
            print("Resturant Lunch Hours")
            print("Name - Start Time - Buffet Availability")
            print("-----------------------")
            for x in range (len(self.lunchlist)):
                print(self.lunchlist[x].name,"-",self.lunchlist[x].time,"pm -",self.lunchlist[x].buffet)
            print("------------")


    def cheapDish(self):
        lp = self.dishlist[0].price
        for x in range (len(self.dishlist)):
            if lp > self.dishlist[x].price:
                lp  = self.dishlist[x].price
        print ("*Lowest price dish - $",lp,self.dishlist[x].name)
        return lp


    def MaxDish(self):
        max = self.dishlist[0].price
        for x in range (len(self.dishlist)):
            if max < self.dishlist[x].price:
               #print(max, self.dishlist[x].price)
               max = self.dishlist[x].price
        print("*Highest price dish - $",max,self.dishlist[x].name)
        return max
            
             

    def avgDish(self):
        print("Average price dishes: ")
        for x in range (len(self.dishlist)):
            if 10 <= self.dishlist[x].price and 25 > self.dishlist[x].price :
                print ("-",self.dishlist[x].name,"$",self.dishlist[x].price )

class Dish:
    def __init__(self,name,price):
        self.name = name 
        self.price = price


class Dessert(Menu):
    def __init__(self,name,dtype,price):
        self.name = name 
        self.dtype = dtype 
        self.price = price

class Lunch:
    def __init__(self,name,time, buffet):
        self.name = name 
        self.time = time
        self.buffet = buffet


print("----------------------------------------------")
print("------------ Welcome to ------------")
print(r1.name,"-",r1.location,"-",r1.contact)
print("-----------------------------------------------")
#menu names
m1 = Menu("Default")
m2 = Menu("Dessert")
m3 = Menu("Lunch")
#Food Items
d1= Dish ("Green Salad",10)
d2= Dish ("Rice & Curry",22)
d3= Dish ("French Fries",7) 
d4= Dish ("Avacado Toast",15) 
d5= Dish ("Calamari",24) 
d6= Dish ("Poutine",30) 
d7= Dish ("Steak",25)
d8= Dish ("Pasta",23) 
d9= Dish ("Noodles",30) 
d10= Dish ("Taco",35)
#dessert names 
ds1 = Dessert("vanila","Ice-cream",13) 
ds2 = Dessert("Black Forest","Cake",30) 
ds3 = Dessert("Apple","Fruit",10) 
#lunch names
l1 = Lunch("Sunday",12, True)    
l2 = Lunch("Saturday",1, True) 
l3 = Lunch("Friday",12, False) 
l4 = Lunch("Tuesday",12, False) 
l5 = Lunch("Wednesday",12, False) 
print("------------------------")
#adding dishes
m1.addDish(d1)
m1.addDish(d2)
m1.addDish(d3)
m1.addDish(d4)
m1.addDish(d5)
m1.addDish(d6)
m1.addDish(d7)
m1.addDish(d8)
m1.addDish(d9)
m1.addDish(d10)
print("-----------------------------")
#adding Dessert
m2.addDessert(ds1)
m2.addDessert(ds2)
m2.addDessert(ds3)
print("-----------------------------")
#adding Lunch
m3.addLunch(l1)
m3.addLunch(l2)
m3.addLunch(l3)
m3.addLunch(l4)
m3.addLunch(l5)
print("-----------------------------")
m1.displayMenu()

#for x in (m1, d1,m2,ds1,m3,l1):
  #x.displayMenu()
#print("-----------------------------")
m1.cheapDish()
m1.MaxDish()
print("-----------------------------")
m1.avgDish()
print("-----------------------------")
r1.addMenu(m1)
print("Number of items -",len((r1.menulist[0]).dishlist))
r1.addMenu(m2)
print("Number of items -",len((r1.menulist[0]).dessertlist))
r1.addMenu(m3)
print("Number of items -",len((r1.menulist[0]).lunchlist))



