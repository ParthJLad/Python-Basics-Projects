# Write a program to print the multiplication table of any number using a while loop.
# (Hint: Start i = 1 and run the loop until i <= 10.)

# Example Output:
# Enter a number: 3
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30

n = int(input("Enter a number:"))

i = 1

while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

print('Question 7: Print the table of a number')