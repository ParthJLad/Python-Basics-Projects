# Write a Python program that takes a number as input and prints:
# “Positive” if number > 0
# “Zero” if number == 0
# “Negative” if number < 0

number = int(input("Enter any number:"))

if(number > 0):
    print("Positive")
elif(number==0):
    print("Zero")
else:
    print("Negative")