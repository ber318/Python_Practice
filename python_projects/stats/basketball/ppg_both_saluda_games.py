import csv

from matplotlib import pyplot as plt

file_name = 'scs_saluda_playoff.csv'

athletes = 1
ppg = 31

#get player names and ppg
with open(file_name) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	ppg_playoff = []
	names = []
	
	for row in reader:
		current_name = row[1]
		names.append(current_name)
		
		current_ppg = int(row[31])
		ppg_playoff.append(current_ppg)
		
	
#print out the column headers and their indices	
#for index, column_header in enumerate(header_row):
#	print(index, column_header)

plt.scatter(names, ppg_playoff, c = 'blue')


plt.title("Points by Player against Saluda", fontsize = 24)
plt.tick_params(axis = 'both', which = 'major', labelsize = 8)

plt.show()
