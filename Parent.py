class Person:
  __name="Unknown"
  __age=-1
  
  def __init__(self, name, age):
    print("Person is coming to alive")
    self.__name = name
    self.__age = age

  def _display(self):
    print("Name = ", self.__name)
    print("Age = ", self.__age)

# derived class

class Student(Person):
  __stdNumber=-1
  __gpa=-1
  
  def __init__(self, name, age, stdnum, gpa):
       Person.__init__(self, name, age)
       print("Student is coming to alive")
       self.__stdNumber = stdnum
       self.__gpa = gpa
       
  def PrintMe(self):
      Person._display(self)
      print("Student# =", self.__stdNumber)
      print("GPA =", self.__gpa)
      
      
s1 = Student("John", 36,112233,4.5)

#s1.PrintMe()



