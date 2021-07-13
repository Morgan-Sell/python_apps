import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # assign color
        self.data[:] = color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


class Square:
    """Initiate the shape"""
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Draw the shape on the canvas."""
        canvas.data[self.x: self.x+self.side, self.y: self.y+self.side] = self.color


class Rectangle:
    """Initiate the shape"""
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """Draw that shape on the canvas."""
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color




canvas = Canvas(10, 12, [0, 255, 0])
square = Square(3, 4, 3, [150, 0, 150])
square.draw(canvas)
rectangle = Rectangle(8, 4, 8, 2, [0, 0, 200])
rectangle.draw(canvas)
canvas.make("test.png")