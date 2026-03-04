# Methods in python

# List are mutable

marks = [95, 98, 90, 88, 70]

print(marks)

marks[1] = 96

print(marks)

# Slicing

print(marks[1:4])

print(max(marks))
print(min(marks))

# methods

marks.append(93)
print(marks)

marks.sort()
print(marks)

marks.remove(70)
print(marks)

marks.pop(4)
print(marks)

marks.insert(1, 66)
print(marks)

marks.reverse()
print(marks)