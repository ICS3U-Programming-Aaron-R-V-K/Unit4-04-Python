# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: April 23, 2025
# Is a guessing number program that loops until the user guess the number

import random


def main():
    # Generate a random number between 1 and 9
    random_number = random.randint(1, 9)

    # While true statement to create a loop
    while True:
        # Get the user input inside the loop as a string
        user_num = input("Guess between 1 and 9: ")

        # Try catch statement if the user enters an invalid input
        try:
            # It type cast the user number from an string to an integer
            num = int(user_num)

            # If the number is less than 0 or more than 9 it will say invalid input
            if num <= 0 or num > 9:
                print("Invalid Input")
            else:

                # If the number is not a random number it will display a message and keep the program repeating
                if num != random_number:
                    print(f"{num}, is not the random number. Try again")
                else:

                    # Else if the user guesses the number it will display a message and stop the program
                    if num == random_number:
                        print("You got the right number")
                    break

        # Exception if input from the user is not an integer
        except Exception:
            print(f"{user_num}, That number is not an integer")


if __name__ == "__main__":
    main()
