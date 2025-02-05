class FleetManagement:
    vehiclelist= []
    def __init__ (self):
        self.vehiclelist = []

    def addVehicle(self, aVehicle):
        self.vehiclelist.append(aVehicle)
        print(aVehicle.make,aVehicle.model,"Vehicle added to the list!","list length :",(len(self.vehiclelist)))

    def RemoveVehicle(self, aVehicle):
        self.vehiclelist.remove(aVehicle)
        print(aVehicle.make,aVehicle.model,"= vehicle Deleted!" )

    def vehicleCount(self):
        car_count = 0
        tr_count = 0
        mt_count = 0
        for x in range (len(self.vehiclelist)):
            #print(self.vehiclelist[x].vtype)
            if "car" == self.vehiclelist[x].vtype:
                car_count = car_count + 1
                print("Car count is = ", car_count)
            elif "truck" == self.vehiclelist[x].vtype:
                tr_count = tr_count + 1
                print("Truck count is = ", tr_count)
            elif "Motorcycle" == self.vehiclelist[x].vtype:
                mt_count = mt_count + 1
                print("Motorcycle count is = ", mt_count)
                
            
        

    def printInfo(self):
        print("-------------------------------------")
        print("Welcome to the Vehicle Management System")
        print("------Vehicle Information-------------")
        print("--------------------------------------")
        print("Vehicle Type | Make | Model | year | Mileage | Fuel Capacity")
        print("--------------------------------------")
        for x in range (len(self.vehiclelist)):
            print(self.vehiclelist[x].vtype,"|",self.vehiclelist[x].make,"|",self.vehiclelist[x].model,
                  "|",self.vehiclelist[x].year,"|",self.vehiclelist[x].mileage,
                  "|",self.vehiclelist[x].fuel_cap) 
            print("--------------------------------------")   

fleet = FleetManagement()

class Vehicle:
    def __init__ (self,make,model,year,mileage,fuel_cap,vtype):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_cap = fuel_cap
        self.vtype = vtype

    def setVehicleType(self):
        return self.VehicleType
        
    def setVehicleType(self,v):
        self.VehicleType= v

vehicle = Vehicle("Audi","A7",2025, 50, 70,"car")

class Car(Vehicle):
    def __init__(self,make,model,year,mileage,fuel_cap,vtype,no_doors,max_speed):
        Vehicle.__init__(self,make,model,year,mileage,fuel_cap,vtype)
        self.no_doors = no_doors
        self.max_speed = max_speed

    def getVehicleType(self):
        return self.VehicleType
        
    def setVehicleType(self,t):
        self.VehicleType = t
    
    def FuelEfficiency(self,fuel_cap):
        fcap = fuel_cap * 0.8
        print (fcap)


c1 = Car("Chevrolet","Blazer",2025, 45,60,"car",4, 200)
c2 = Car("Hyundai","Elantra",2023, 51,66, "car",4, 220)

c1.setVehicleType("Car")
print(c1.getVehicleType())


class Truck(Vehicle):
    def __init__(self,make,model,year,mileage,fuel_cap,vtype,cargo_cap):
        Vehicle.__init__(self,make,model,year,mileage,fuel_cap,vtype)
        self.cargo_cap = cargo_cap

    def getVehicleType(self):
        return self.VehicleType
        
    def setVehicleType(self,t):
        self.VehicleType= t
       
    def FuelEfficiency(self,fuel_cap):
        fcap = fuel_cap * 0.8
        print (fcap)

t1 = Truck("Hyundai","Santa Cruz",2025, 55, 65,"truck",52.1)
t1.setVehicleType("Truck")
print(t1.getVehicleType())


class Motorcycle(Vehicle):
    def __init__(self,make,model,year,mileage,fuel_cap,vtype,engine_cc):
        Vehicle.__init__(self,make,model,year,mileage,fuel_cap,vtype)
        self.engine_cc = engine_cc
       
    def getVehicleType(abc):
        return abc.VehicleType
        
    def setVehicleType(abc,t):
        abc.VehicleType= t

    def FuelEfficiency(self,fuel_cap):
        fcap = fuel_cap * 0.8
        print (fcap)

m1 = Motorcycle("Honda","nc750x",2024, 55, 14,"Motorcycle",745)

m1.setVehicleType("MotorCycle")
print(m1.getVehicleType())


fleet.addVehicle(c1)
fleet.addVehicle(c2)
fleet.addVehicle(t1)
fleet.addVehicle(m1)
fleet.printInfo()
#fleet.RemoveVehicle(c1)
fleet.vehicleCount()
fleet.printInfo()
  