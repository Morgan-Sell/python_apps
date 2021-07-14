from canvas import Canvas
from shapes import Square, Rectangle

canvas = Canvas(10, 12, [0, 255, 0])
square = Square(3, 4, 3, [150, 0, 150])
square.draw(canvas)
rectangle = Rectangle(8, 4, 8, 2, [0, 0, 200])
rectangle.draw(canvas)
canvas.make("test.png")

# get canvas dimensions
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Create a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas using the provided data.
canvas = Canvas(canvas_width, canvas_height, colors[canvas_color])


while True:
    shape_type = input("Which shape would like you to draw? Square or rectangle? Enter quit to quit. ")

    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter rectangle width: "))
        rec_height = int(input("Enter rectangle height: "))
        red = int(input("How much red would you like (0 - 255)? "))
        blue = int(input("How much blue (0 - 255)? "))
        green = int(input("How much green (0 - 255)? "))

        r1 = Rectangle(rec_x, rec_y, rec_width, rec_height, (red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        sq_x = int(input("Enter x of the square: "))
        sq_y = int(input("Enter y of the square: "))
        sq_side = int(input("Enter length of square side: "))
        red = int(input("How much red would you like (0 - 255)? "))
        blue = int(input("How much blue (0 - 255)? "))
        green = int(input("How much green (0 - 255)? "))

        s1 = Square(sq_x, sq_y, sq_side, (red, green, blue))
        s1.draw(canvas)

    if shape_type.lower() == "quit":
        break

canvas.make("canvas.png")