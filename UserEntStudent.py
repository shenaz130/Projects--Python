class Student:
    def __init__(self, sid, name, score):
        self.sid = sid
        self.name= name
        self.score = score


class CourseManager:
    studentlist = []

    def __init__(self):
        self.studentlist= []

    def addStudent(self):
        index = self.findStudentbyID(sid)
        if sid == -1:
            sid= int(input("Enter the student ID:"))
            sname= input("Enter the student name:")
            sscore= input("Enter the student Score:")
            s1 = Student(sid,sname,sscore)
            self.studentlist.append(s1)
            print ("New Student Added")
            print("Length",len(self.studentlist))
        else:
            print("This student already there!")

    def findStudentbyID(self,sid):
        for x in range (len(self.studentlist)):
            if sid == self.studentlist[x].sid:
                print("ERROR: STUDENT ALREADY THERE")
                print(self.studentlist[x].sid,self.studentlist[x].name)
                return x
        return -1
    
c1= CourseManager()
c1.addStudent()


