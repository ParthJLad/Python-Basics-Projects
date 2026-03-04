# take a number as input, convert it to a float, and print both the original and converted values with their datatypes

number = int(input("Enter any number:"))

original = number
converted = float(number)

print('The original value is', original, 'and the datatype is', type(original))
print('The converted value is', converted, 'and the datatype is', type(converted))
