# Write a program that prints numbers 1 to 10, but skips the number 7 using the continue statement.

for num in range(1, 11):
    if num == 7:
        continue
    print(num)
