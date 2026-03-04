# Dictioary basics in python

student = {
    "name" : "Parth Lad",
    "age" : 25,
    "city" : "Bilimora",
    "gender" : "Male"
}

student["age"] = 24
student["favSubject"] = "Computer"

print(student.pop("gender"))
print(student)
print(type(student))
print(student["name"])
print(student["age"])
print(student["city"])

print(student.keys())
print(student.values())
print(student.items())