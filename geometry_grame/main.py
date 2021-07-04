import turtle

# Create a canvas instance
myturtle = turtle.Turtle()

# Go to the specified coordinates
myturtle.penup() # prevent line from being drawn
myturtle.goto(50, 75)

myturtle.pendown() # enables drawing
myturtle.forward(100) # move 100 pixels
myturtle.left(90) # turn 90 degrees
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()