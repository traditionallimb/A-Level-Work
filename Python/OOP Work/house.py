class House:
	# constructor class
	def __init__(self, windows, stories, number, st_name):
		# member variable declaration
		self.num_windows = windows
		self.num_stories = stories
		self.house_number = number
		self.street_name = st_name

	# function to print number of windows
	def print_window_count(self):
		print(self.num_windows)

	# function to return the house value
	def get_value(self):
		value = f"Value: £{self.num_stories * self.num_windows * 10000}"
		return value

	# function to return the address of the house
	def get_address(self):
		address = f"Address: {self.house_number} {self.street_name}"
		return address


# object creation
seven_barnaby_road = House(14, 1, "7", "Barnaby Road")
print(seven_barnaby_road.get_address())
print(seven_barnaby_road.get_value())

nine_swindon_ave = House(20, 2, "9", "Swindon Avenue")
print(nine_swindon_ave.get_address())
print(nine_swindon_ave.get_value())

one_finley_st = House(12, 1, "1", "Finley Street")
print(one_finley_st.get_address())
print(one_finley_st.get_value())
