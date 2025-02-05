class Person:
    def __init__(self,pid,name,age,height,weight):
        self.pid= pid
        self.name = name 
        self.age = age
        self.height = height
        self.weight = weight

    def _getTBW(self):
        mtbw = 2.447 -(0.9156 *self.age)+ (0.1074 * self.height) +(0.3362 *self.weight)
        ftbw = -2.097 -(0.1069 *self.height)+  +(0.2466 *self.weight)
        return mtbw
        return ftbw


class Female(Person):
    def __init__(self,pid,name,age,height,weight):
       Person.__init__(self,pid,name,age,height,weight)

    def getTBWF(self):
        Person._getTBW(self)
        print(self.name,"'s Total body water level is = ",self._getTBW())

class Male(Person):
    def __init__(self,pid,name,age,height,weight):
       Person.__init__(self,pid,name,age,height,weight)

    def getTBWM(self):
        Person._getTBW(self)
        print(self.name, "'s Total body water level is = ",self._getTBW())


    
f1= Female(112,"Jane",25,165,50)
m1= Male(155,"John",30,175,80)
f1.getTBWF()
m1.getTBWM()



