class Student:
    def __init__(self, sid, name, score):
        self.sid = sid
        self.name= name
        self.score = score

s1 = Student (12345,"John",34.5)
s2 = Student (12333,"Dave",96.0)
s3 = Student (12226,"Mark",66.9)
s4 = Student (12826,"Sasha",100.0)
print(s1.sid)

class CourseManager:
    studentlist = []

    def __init__(self):
        self.studentlist= []

    def addStudent(self, aStudent):
        sid = self.findStudent(aStudent.sid)
        if sid == -1:
            self.studentlist.append(aStudent)
            print ("New Student Added")
            print("Length",len(self.studentlist))
        else:
            print("This student already there!")

    def findStudent(self,sid):
        for x in range (len(self.studentlist)):
            if sid == self.studentlist[x].sid:
                print("ERROR: STUDENT ALREADY THERE")
                print(self.studentlist[x].sid,self.studentlist[x].name)
                #c1.displayStudent()
        return -1
    
    def findStudentbyName(self,name):
        for x in range (len(self.studentlist)):
            if name == self.studentlist[x].name:
                print("ERROR: STUDENT ALREADY THERE")
                print(self.studentlist[x].sid,self.studentlist[x].name)
            else:
                return
            

    def removeStudent(self,aStudent):
        index = self.findStudent(aStudent.sid)
        print (index)
        if index == -1:
            #print("###")
            self.studentlist.remove(aStudent)
            print (aStudent.name, " Deleted!")
            print("Length",len(self.studentlist))
        else:
            print("Invalid student index!")
    
    def displayStudent(self):
        print("------------------------------------")
        print("Students are :")
        print("------------------------------------")
        for x in range (len(self.studentlist)):
            print("ID -",self.studentlist[x].sid,",","Name -",self.studentlist[x].name,",","Score -",self.studentlist[x].score)
            print("------------------------------------")

    def findAvgScore(self):
        tot = 0
        count = 0
        for x in range (len(self.studentlist)):
            tot = tot+ self.studentlist[x].score
            count = count +1
        print("The class average = ", tot/count)

    def findMaxScore(self):
        max = self.studentlist[0].score
        for x in range (len(self.studentlist)):
            if max <= self.studentlist[x].score:
                max = self.studentlist[x].score
        print("The Student with the highest score :")
        print(self.studentlist[x].sid,self.studentlist[x].name,max)

    



c1= CourseManager()
c1.addStudent(s1)
c1.addStudent(s2)
c1.addStudent(s3)
c1.addStudent(s4)
c1.findStudent(12333)
c1.findStudentbyName("Dave")
#c1.findStudentbyName("hhh")
c1.findAvgScore()
c1.findMaxScore()
#c1.removeStudent(s3)
c1.displayStudent()