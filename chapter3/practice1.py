# Write a program that takes your favorite food name as input and prints:
# The Middle 3 characters
# The last 2 characters

food = input('Enter your favorite food:')

mid = len(food)//2
output = food[mid-1:mid+2]

print(output)

print(food[-2:])