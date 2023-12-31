# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gl_tZfVjsMNR3FdRrAMc4V30SVsaBGyF
"""

import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    print("Dice Rolling Simulator")

    while True:
        sides = int(input("Enter the number of sides on the dice (4/6/8/10/12/20): "))

        if sides in (4, 6, 8, 10, 12, 20):
            roll_result = roll_dice(sides)
            print(f"The dice rolled: {roll_result}")
        else:
            print("Invalid number of sides. Please choose from 4, 6, 8, 10, 12, or 20.")

        roll_again = input("Roll the dice again? (yes/no): ")
        if roll_again.lower() != 'yes':
            print("Dice rolling simulator closing.")
            break

if __name__ == "__main__":
    main()