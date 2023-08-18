"""Calculates the number of paint cans to paint a given area"""

from math import ceil

def paint_calc(height, width, cover):

    area = height * width
    number_of_cans = ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint.")

# Define a function called paint_calc() so that the code below works.
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
