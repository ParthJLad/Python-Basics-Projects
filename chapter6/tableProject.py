# Mini Project – Multiplication Table
# Goal: Print the multiplication table of a number using a loop.

n = int(input("Please Enter a number: "))

i = 1
while i <= 10:
    print(f"{n} x {1} = {n * i}")
    i += 1
