class Human:
	def __init__(self):
		self.__firstName = "Jane"
		self.__surname = "Doe"
		self.__eyeColour = "Green"
		self.__hairColour = "Red"
		self.__height = 160
		self.__weight = 70

	def get_first_name(self):
		return self.__firstName

	def get_surname(self):
		return self.__surname

	def get_eye_colour(self):
		return self.__eyeColour

	def get_hair_colour(self):
		return self.__hairColour

	def get_height(self):
		return self.__height

	def get_weight(self):
		return self.__weight

	def set_first_name(self, firstName):
		self.__firstName = firstName

	def set_surname(self, surname):
		self.__surname = surname

	def set_eye_colour(self, eyeColour):
		possibleEyeColours = ["Black", "Hazel", "Blue", "Green", "Red"]
		if eyeColour not in possibleEyeColours:
			print("Invalid eye colour")
			return None
		self.__eyeColour = eyeColour

	def set_hair_colour(self, hairColour):
		self.__hairColour = hairColour

	def set_height(self, height):
		if height < 0 or height > 272:
			print("Invalid height")
			return None
		self.__height = height

	def set_weight(self, weight):
		if weight < 0 or weight > 645:
			print("Invalid weight")
			return None
		self.__weight = weight

	def bmi(self):
		heightInCm = self.__height / 100
		return self.__weight / (heightInCm * heightInCm
								)

	def print_all(self):
		print(f"Name: {self.__firstName} {self.__surname}\nEye Colour: {self.__eyeColour}\nHair Colour: {self.__hairColour}\nHeight: {self.__height}cm\nWeight: {self.__weight}kg")


willCarter = Human()

willCarter.set_first_name("Will")
willCarter.set_surname("Carter")
willCarter.set_eye_colour("gone")
willCarter.set_hair_colour("Dirty Blonde")
willCarter.set_height(176)
willCarter.set_weight(59)

willCarter.print_all()

print(willCarter.bmi())