# A2 Turtle Assignment
# Starter code by David Johnson
# For COMP1010 University of Utah
#
# Assignment written by: Sejin Yoon, u1311019

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
triangle.goto(200,0)
triangle.goto(100,200)
triangle.goto(0,0)
turtle.done()



# A2 b)
# Make a turtle named zigzag and use that turtle to draw
# a blue zigzag shape starting at position x = -100 and y = 100.
# See the assignment for an example picture. You must use a
# loop to repeat the pattern for 8 peaks.
# The turtle should not leave any other lines except the zig zag.


import turtle
window = turtle.Screen()
zigzag = turtle.Turtle()
zigzag.color('blue')
zigzag.penup()
zigzag.goto(-100,100)
zigzag.pendown()
zigzag.width(1)
zigzag.left(60)
for _ in range(8):
    zigzag.forward(50)
    zigzag.right(120)
    zigzag.forward(50)
    zigzag.left(120)
turtle.done()



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
spiral.penup()
spiral.goto(0,-100)
spiral.pendown()
spiral.width(1)
for x in range(1,200,5):
    spiral.forward(x)
    spiral.left(90)
turtle.done()



# A2 d)
# Add a new turtle. Draw a nice picture of your own design.
# There should be different colors and sections that require
# the pen to go back up and back down.
# Leave the window up until it is clicked


color = ["red","purple","blue","green","orange","yellow"]
colorIndex = 0

import turtle
window = turtle.Screen()
turtle.bgcolor("black")
Apple = turtle.Turtle()
Apple.speed(10)
Apple.shape("circle")
Apple.color('red')
Apple.penup()
Apple.goto(50,50)
Apple.pendown()
appleWidth = 3
dotSize = 2
for x in range(1, 200, 3):
    Apple.pencolor(color[colorIndex%6])
    Apple.forward(x)
    Apple.left(120)
    Apple.dot(dotSize,"black")
    Apple.right(60)
    Apple.dot(dotSize,"black")
    Apple.width(appleWidth)
    colorIndex += 1

    # It increases width AND dotSize in every loop
    appleWidth += 0.1
    dotSize += 2
turtle.exitonclick()


