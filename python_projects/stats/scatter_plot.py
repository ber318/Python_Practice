import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#how to set a specific color
#plt.scatter(x_values, y_values, edgecolor = 'none', c = 'red', s = 40)

#how to set a gradient of colors
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 40)
plt.title("Square Numbers")
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

#set the range for the axis
plt.axis([0,1100,0,1100000]) 

#show it on execution
plt.show()

#save to a file
#plt.savefig('squares_plot.png', bbox_inches = 'tight')

