# 
from random import randint


class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def falls_in_rectangle(self, rectangle):
		if rectangle.lowleft.x < self.x < rectangle.upright.y \
		and rectangle.lowleft.x < self.y < rectangle.upright.y:
			return True
		else:
			return False

	def distance_from_points(self, point):
		return ((self.x - point.x)**2 + (self.y - point.y**2)) ** 0.5

class Rectangle:

	def __init__(self, lowleft, upright):
		self.lowleft = lowleft
		self.upright = upright

	def  area(self):
		width = self.upright.x - self.lowleft.x
		height = self.upright.y - self.lowleft.y
		return width * height


if __name__ == "__main__":

	rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), \
		Point(randint(10, 19), randint(10, 19)))

	print("Rectangle Coordinates: ", rectangle.lowleft.x, ",", rectangle.lowleft.y, \
		"and", rectangle.upright.x, ",", rectangle.upright.y)

	user_point = Point(float(input("Guess X: ")), \
				float(input("Guess Y: ")))
	user_area = float(input("Guess rectangle area: "))

	print("You point was inside the rectangle: ", user_point.falls_in_rectangle(rectangle))
	print("Your area was off by: ", rectangle.area() - user_area)











