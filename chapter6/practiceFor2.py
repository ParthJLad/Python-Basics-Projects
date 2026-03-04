# Write a program to print numbers from 1 to 50, but print "Parth Lad"
# instead of numbers that are multiples of 5.
# Example Output: 1 2 3 4 Parth Lad 6 7 8 9 Parth Lad ...

for item in range(1, 51):
    if item % 5 == 0:
        print("Parth Lad")
    else:
        print(item)
    item += 1
