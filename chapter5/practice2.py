# You are given a list of programming languages:
# ["Python", "Java", "C++", "Python", "Java", "C"]
# Convert it into a set and print how many unique languages Parth knows.

programmingLang = ["Python", "Java", "C++", "Python", "Java", "C"]
print(type(programmingLang))

# How to convert list in set

programmingSet = set(programmingLang)
print(type(programmingSet))

print(programmingSet)

print("Parth Knows these many languages", len(programmingSet))