# Mini Project – Countdown Timer (with 1-second gap)
# Goal:
# Print a countdown before something “exciting” happens (like “Launching...” or
# “Happy New Year!”).
# Concepts Used: for loop, range(), and the time module.

import time

count = int(input("Enter the counter num: "))

print("\n Countdown Starts Now: ")

for i in range(count, 0 , -1):
    print(i)
    time.sleep(1)

print("\n WOHOOO! Happy New Year")

