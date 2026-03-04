# Write a program that prints the sum of first n natural numbers.
# For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.
# (Hint: Keep a running total inside the loop.)

n = int(input("Please enter a number:"))

sum = 0

while n >= 1:
    sum += n
    n -= 1


print("Sum", sum)
print("n", n)
print("Question 4 : The sum of first n natural numbers")
