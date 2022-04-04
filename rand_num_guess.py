#!/usr/bin/env python3
# Created By: Titwech Wal
# Date: April.1. 2022

# the program asks the user for a number
# then tell them if they are correct
# program uses random generator

from colorama import Fore
import random


def main():
    # get user input
    num_guess = int(input("Guess the random number: "))
    print("")

    # a number between 1 and 100
    random_variable = random.randint(1, 100)

    # check if number is correct or incorrect
    if num_guess == random_variable:
        print(Fore.GREEN + "You guessed right")

    else:
        print(Fore.RED + "You guessed wrong the number is: {}"
              .format(random_variable))


if __name__ == "__main__":
    main()
