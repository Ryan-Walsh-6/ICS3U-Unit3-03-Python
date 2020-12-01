#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: November 2020
# this program checks to see if the number guessed is the random number


import random


def main():
    # this program checks to see if the number guessed is the random number

    # input
    guessed_number = int(input("Enter a number(between 0-9): "))
    print("")
    random_number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    if guessed_number == random_number:
        print("Congratulations! You guessed the right number!")
    else:
        print("Not the correct number. Try again")
        print("")
        print("The correct number was:{}".format(random_number))


if __name__ == "__main__":
    main()
