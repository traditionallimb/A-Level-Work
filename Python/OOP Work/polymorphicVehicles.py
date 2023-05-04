class Vehicle:
	def __init__(self, colour: str, topSpeed: int, carPrice: int):
		self._colour = colour  # private
		self._topSpeed = topSpeed  # private
		self._carPrice = carPrice

	def get_price(self):
		return self._carPrice

	def set_price(self, newCarPrice):
		self._carPrice = newCarPrice

	def get_colour(self):
		return self._colour

	def set_colour(self, newColour):
		self._colour = newColour

	def get_top_speed(self):
		return self._topSpeed

	def set_top_speed(self, newTopSpeed):
		self._topSpeed = newTopSpeed


class Car(Vehicle):
	def __init__(self, colour: str, topSpeed: int, carPrice: int, mediaSuite: bool, leatherSeats: bool):
		super().__init__(colour, topSpeed, carPrice)
		self.__mediaSuite = mediaSuite
		self.__leatherSeats = leatherSeats

	def get_price(self):
		if self._carPrice > 1000000:
			price = 1000000
		else:
			price = self._carPrice
		if self.__mediaSuite:
			price += 2000
		if self.__leatherSeats:
			price += 5000
		return price


class Yacht(Vehicle):
	def __init__(self, colour: str, carPrice: int, numMasts: int):
		super().__init__(colour, )


test = Vehicle("Red", 140, 500000)
print(f"{test.get_price()}\n{test.get_colour()}\n{test.get_top_speed()}")

miniCooper = Car("Orange", 280, 25000, True, False)
print(f"£{miniCooper.get_price()}")

