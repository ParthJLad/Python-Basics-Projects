# write a program that takes two numbers and prints:

# sum , difference and product

# whether the first number is greater then second

number1 = int(input('Enter number 1:'))
number2 = int(input('Enter number 2:'))

sum = number1 + number2

print("The sum is", sum)

difference = number1 - number2

print("The difference is", difference)

product = number1 % number2

print("The product is", product)

x = number1 > number2

print('first number 1 is greater than number 2 ?', x)