# Mini Project – Guess the Number Game
# Concepts Used: while loop and user input.

n = int(input("Guess the correct number from 1 t0 10: "))

while n <= 10:
    if(n == 5):
        print("Congratulations, Parth! You guessed it right 🎉")
        break
    else:
        print("Wrong guess! Try again.")
        n = int(input("Guess again: "))
