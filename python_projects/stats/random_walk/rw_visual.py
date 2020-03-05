import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Make a random walk, and plot the points
while True:
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	#point_numbers has a list from 1 to 5000
	#it then does a blue gradient based on the point's order in the walk
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s = 15)
	
	#emphasize the beginning and ending points
	plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)
	
	#remove the axes
	#plt.axes().get_xaxis().set_visible(False)
	#plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
		
		

