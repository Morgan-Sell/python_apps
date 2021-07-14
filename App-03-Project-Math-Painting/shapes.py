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