#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program runs a dice game program

import random


def main():
    # this function uses a while loop
    random_roll1 = random.randint(1, 6)
    random_roll2 = random.randint(1, 6)
    loop_counter = 0

    # this function runs the "Dice Game" program
    # input
    print("Let's roll some dice!")

    # process and output
    while True:
        loop_counter = loop_counter + 1
        if random_roll1 == random_roll2:
            break
    print("You got a double! {0},{1}".format(random_roll1, random_roll2))
    print("\nIt took you {0} rolls!".format(loop_counter))
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
