#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program calculates the area of a triangle


def calculate_area(base, height):
    # calculates the area of a triangle

    area = base * height / 2
    float_area = "{:.1f}".format(area)

    # output
    print("The area is: {0} cm²".format(float_area))


def main():
    try:
        base_from_user = int(input("Enter the base of the triangle"
                                   "(cm): "))
        height_from_user = int(input("Enter the height of the triangle"
                                     "(cm): "))
        print("")

        # calls function
        calculate_area(base_from_user, height_from_user)

    except ValueError:
        print("This was not a number")


if __name__ == "__main__":
    main()
