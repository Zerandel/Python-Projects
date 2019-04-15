#!/usr/bin/env python3

# Find Cost of Tile to Cover W x H Floor

# The program calculates the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

# Firstly, we define "width" , "height" and "cost".

width = float(input("The width of tile is: "))

height = float(input("The height of tile is: "))

cost = float(input("The cost of tile is: "))

# Then we create the program, using these features in a formula to calculate the total cost of tile.

print("The total cost of tile of %.2f x %.2f floor is: %.2f " % (width, height, width * height * cost))
