# Sets basic in python

subjects = {"Maths", "Physics", "Chemistry", "English", "Maths"}

print(type(subjects))
print(subjects)

empty_set = set()
print(type(empty_set))

subjects.add("Hindi")
print(subjects)

subjects.remove("Maths")
print(subjects)
