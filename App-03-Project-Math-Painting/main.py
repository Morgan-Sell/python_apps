import numpy as np
from PIL import Image

class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        data = np.zeros((self.side, self.side, 3), dtype=np.uint8)
        data[:] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        pass


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self, imagepath):
        data = np.zeros((self.height, self.width, self.color), dtype=np.unit8)
        data[:] = self.color

        img = Image.fromarray(data, 'RGB')
        img.save(imagepath)