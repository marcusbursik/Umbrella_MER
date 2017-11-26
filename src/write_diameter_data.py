"""
Name: write_diameter_data
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import csv					# for reading/writing csv files
import numpy as np			# numpy for array operations

def write_diameter_data(D1,D2, diameters_csv_file):
	"""
	.csv file = write_diameter_data(D1, D2, diameters_csv_file)

	Description: This function creates a matrix of the diameter data, 
	 and writes it out to a .csv file.

	Input: 
	 'D1' - A vector of minimum diameters (km) 
	 'D2' - A vector of maximum diameters (km)
	 'diameters_csv_file' - A filename for the .csv output to be saved to

	Output:
	 Writes out a csv file to the results folder, or that specified in 
		output csv filename
	"""

	# Pre-allocate space for the matrix of diameter results
	diameters_matrix = np.zeros([len(D1),2])

	# Assign each column in the matrix to the vectors of diameters
	diameters_matrix[:,0] = D1
	diameters_matrix[:,1] = D2

	# Create the file that will be written to
	f = open(diameters_csv_file, 'w')
	writer = csv.writer(f)
	# Write the header row 
	writer.writerow(['D1, min (km)', 'D2, max (km)'])

	# Write the data into the csv file
	for values in diameters_matrix:
		writer.writerow(values)
	
	# Close the file when done writing
	f.close()
