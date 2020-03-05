#import for the choice() method
from random import choice

#class for the randomwalk
class RandomWalk():
	
	#constructor method
	def __init__(self, num_points = 5000):
		self.num_points = num_points
		
		#two more class variables for the points for the walk
		self.x_values = [0]
		self.y_values = [0]
		
	def get_step(self):
		direction = choice([1,-1])
		distance = choice([0,1,2,3,4])
		step = direction * distance
		return step
		
	def fill_walk(self):
		#keep adding steps until you reach 5000
		while len(self.x_values) < self.num_points:
			#decide which direction to go and how far to go
			x_step = self.get_step()
			y_step = self.get_step()
			
			#if they dont take a step than skip
			if x_step == 0 and y_step == 0:
				continue
				
			#calculate the next x and y values and add them to the lists	
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
			
			
			
