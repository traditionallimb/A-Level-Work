from math import pi


class Shape:
	def __init__(self, width: int, height: int):
		self._width = width  # protected
		self._height = height  # protected

	def get_area(self) -> int:
		return 0

	def get_perimeter(self) -> int:
		return 0


class Rectangle(Shape):
	def __init__(self, width: int, height: int):
		super().__init__(width, height)

	def get_area(self) -> int:
		return self._width * self._height

	def get_perimeter(self) -> int:
		return (self._width * 2) + (self._height * 2)


class Square(Rectangle):
	def __init__(self, height):
		super().__init__(height, height)


class Circle(Shape):
	def __init__(self, radius):
		super().__init__(radius * 2, radius * 2)
		self.__radius = radius

	def get_area(self) -> int:
		return (self.__radius ** 2) * pi

	def get_perimeter(self) -> int:
		return self.__radius * pi


class Triangle(Shape):
	def __init__(self, side, height, side1, side2):
		super().__init__(side, height)
		self.__side1 = side1
		self.__side2 = side2

	def get_area(self) -> float:
		return (self._width * self._height) / 2

	def get_perimeter(self) -> int:
		return self._width + self.__side1 + self.__side2


loopCtrl = 1
while loopCtrl == 1:
	try:
		usrOptShape = int(input("Which shape do you want?\n\t1. Square\n\t2. Rectangle\n\t3. Circle\n\t4. Triangle\n> "))
	except ValueError:
		print("That isn't a number")
		loopCtrl = 1


	if usrOptShape == 1:
		usrOptSquareSide = int(input("Enter the value of the side of your square. > "))
		square = Square(usrOptSquareSide)
		print(f"This shapes area is: {square.get_area()}\nThis shapes perimeter is: {square.get_perimeter()}")
	elif usrOptShape == 2:
		usrOptRectangleSide1 = int(input("Enter the value of one of the sides of your rectangle. > "))
		usrOptRectangleSide2 = int(input("Enter the value of the other side of your rectangle. > "))
		rectangle = Rectangle(usrOptRectangleSide1, usrOptRectangleSide2)
		print(f"This shapes area is: {rectangle.get_area()}\nThis shapes perimeter is: {rectangle.get_perimeter()}")
	elif usrOptShape == 3:
		usrOptCircleRadius = int(input("Enter the value of the radius of your circle. > "))
		circle = Circle(usrOptCircleRadius)
		print(f"This shapes area is: {circle.get_area()}\nThis shapes perimeter is: {circle.get_perimeter()}")
	elif usrOptShape == 4:
		usrOptTriangleSide1 = int(input("Enter the value of the first side of your triangle. > "))
		usrOptTriangleSide2 = int(input("Enter the value of the second side of your triangle. > "))
		usrOptTriangleSide3 = int(input("Enter the value of the third side of your triangle. > "))
		triangle = Triangle(usrOptTriangleSide1, usrOptTriangleSide2, usrOptTriangleSide3)
		print(f"This shapes area is: {triangle.get_area()}\nThis shapes perimeter is: {triangle.get_perimeter()}")

