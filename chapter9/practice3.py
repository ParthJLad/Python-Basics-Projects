# Create class Student that takes 3 marks & has a method average().

class Student:

    def __init__(self, name, listOfMarks):
        self.name = name
        self.listOfMarks = listOfMarks

    def average(self):
        sum = 0
        for eachValue in self.listOfMarks:
            sum += eachValue

        avg = sum / len(self.listOfMarks)
        print(self.name, "Total Average of result is:", avg)



s1 = Student("Parth", [90, 99, 100]) 
s1.average()
s2 = Student("Veer", [80, 95, 99]) 
s2.average()
s3 = Student("Smit", [90, 85, 70]) 
s3.average()