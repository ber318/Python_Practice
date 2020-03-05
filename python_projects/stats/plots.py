import matplotlib.pyplot as plt


#x values
input_values = [1, 2, 3, 4, 5]
#y values
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth = 5)

#Set Chart Title and Label Axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

#Set Size of Tick Labels
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()
