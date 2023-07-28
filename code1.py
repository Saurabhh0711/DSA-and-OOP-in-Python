class student:

    school = 'Indian_school'

    def __init__(self,marks,grade):
        self.marks = marks
        self.grade = grade


    def start1(self):
        print("Student 1 marks and grade are",self.marks,self.grade)
    
    def start2(self):
        print("Student 2 marks and grade are",self.marks,self.grade)

    def compare_marks(self,other):
        if self.marks > other.marks:
            return True
        else:
            return False
        
    @classmethod  
    def info(clr):
        return clr.school
    
    @staticmethod
    def extra():
        print("School info")


s1 = student(50,2)
# s1.marks = 10
s2 = student(20,4)
print(student.info())

s1.start1()
s2.start2()

if s1.compare_marks(s2):
    print("s1 wins")
else:
    print("s2 wins")

student.extra()
