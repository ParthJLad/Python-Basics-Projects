# init in python

class Student:
    schoolName = "TATA School"

    def __init__(self, name, course):
        self.name = name
        self.course = course
        print("Whenever new object is created i am call automatically")
        # print(self)

s1 = Student("Parth", "BE") # init method will be called
print("Student 1", s1.name)
print("Student 1", s1.course)

s2 = Student("Veer", "BSC")
print("Student 1", s2.name)
print("Student 1", s2.course)