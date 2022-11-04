#!/usr/bin/env python3

# Created by: Lucas LeBlanc
# Created on: Nov 2022
# This program adds each whole number that goes up to the users number


def main():
    # This function adds each whole number that goes up to the users number
    counter = 0
    the_sum = 0

    # Input
    integer_a_s = input("Enter a positive number: ")
    print("")

    # Process and Output
    try:
        integer_a_i = int(integer_a_s)
        while counter < integer_a_i:
            counter = counter + 1
            the_sum = the_sum + counter
        print(
            "The sum of all positive numbers from 1 to {0} is {1}.".format(
                integer_a_s, the_sum
            )
        )

    except Exception:
        print("Invalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
