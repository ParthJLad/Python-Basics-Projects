# Ask the user for their 3 favorite movies and store them in a list.

movie1 = input("Enter you fav movie mo 1:")
movie2 = input("Enter you fav movie mo 2:")
movie3 = input("Enter you fav movie mo 3:")

movies_list = []
movies_list.append(movie1)
movies_list.append(movie2)
movies_list.append(movie3)
print(movies_list)

# Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and lowest marks using max() and min().

marks = (87, 64, 33, 95, 76)
max = max(marks)
min = min(marks)

print(max)
print(min)

# Write a program to check grade based on marks (A/B/C/D) using if-elif-else.

marks = int(input("Enter your marks:"))

if(marks > 95):
    print("Youe grade is A")
elif(marks > 85):
    print("Youe grade is B")
elif(marks > 75):
    print("Youe grade is C")
else:
    print("Your grade is D")
