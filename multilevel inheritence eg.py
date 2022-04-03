class student:
    def __init__(self, name, mark1,mark2):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2

    def getdetails(self):
        self.name = input("enter the name")
        self.mark1 = int(input("enter the mark 1"))
        self.mark2 = int(input("enter the mark 2"))
    def putdetails(self):
        print(self.name,self.mark1,self.mark2)

class ScienceTeacher(student):
    
    def getscience(self):
        self.subject = input("enter the subject")
        self.topic = input("enter the  topic")
    def sciencedetails(self):
        print(self.subject,self.topic)


class SocialTeacher(ScienceTeacher):
    
    def getsocial(self):
        self.teachername = input("enter the teacher name")
        self.classhours = int(input("enter the  no. of hours"))
    def socialdetails(self):
        print(self.teachername,self.classhours)



obj =SocialTeacher('','','')
obj.getdetails()
obj.putdetails()
obj.getscience()
obj.sciencedetails()
obj.getsocial()
obj.socialdetails()
