# A2 Turtle Assignment
# Starter code by David Johnson
# For COMP1010 University of Utah
#
# Assignment written by: __________________

# Use the turtle module
import turtle

# Create a screen to draw on
window = turtle.Screen()

# A2 a)
# Make a turtle named triangle and use that turtle to draw
# a triangle with one corner at position x = 0 and y = 0

import turtle
window = turtle.Screen()
triangle = turtle.Turtle()
triangle.width(2)
triangle.goto(0,0)
triangle.dot()
triangle.goto(200,0)
triangle.dot()
triangle.goto(100,200)
triangle.dot()
triangle.goto(0,0)





# A2 b)
# Make a turtle named zigzag and use that turtle to draw
# a blue zigzag shape starting at position x = -100 and y = 100.
# See the assignment for an example picture. You must use a
# loop to repeat the pattern for 8 peaks.
# The turtle should not leave any other lines except the zig zag.







# A2 c)
# Make a turtle named spiral and use that turtle to draw
# a green square spiral shape with the center starting at
# position x = 0 and y = -100.
# See the assignment for an example picture.
# You must use a loop to grow the spiral.
# The turtle should not leave any other lines except the spiral.

import turtle
window = turtle.Screen()
spiral = turtle.Turtle()
spiral.color('green')
spiral.setup(0, -100)
spiral.width(1)
for x in range(1,200,5):
    spiral.forward(x)
    spiral.left(90)
spiral.exitonclick()


# A2 d)
# Add a new turtle. Draw a nice picture of your own design.
# There should be different colors and sections that require
# the pen to go back up and back down.

# Leave the window up until it is clicked
window.exitonclick()