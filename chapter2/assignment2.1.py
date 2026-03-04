# Write a program that takes total bill amount and number of friends as input
# Calculate how much each person will pay.
# Also print the data type of each variable used.

bill = int(input("Enter the total bill amount:"))

person = int(input("How many you are?:"))

pay = bill / person

print("Each person will pay", pay , "rupess")

print(type(bill))
print(type(person))
print(type(pay))
