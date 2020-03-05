from random import randint

class Die():
	def __init__(self, num_sides = 6):
		self.num_sides = num_sides
		
	def roll(self):
		#returns a value between 1 and num_sides
		return randint(1, self.num_sides)
