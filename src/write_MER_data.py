"""
Name: write_MER_data
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import numpy as np			# numpy for array operations
import csv					# for reading/writing csv files

def write_MER_data(tss, A, maxPh, Ph, rhobar, rhogas, MERpa, mass, cloudtype, MER_csv_file):
    """
    .csv file =  write_MER_data(tss, A, MERpl, MERpli, MERpa, MERpai, cloudtype, MER_csv_file):

    Description: This function creates a matrix of the results on MER 
     with time, or estimated mass, and writes it out to a .csv file.

    Input:
     'tss' - Vector of number of seconds since eruption start
     'A' - Vector of area of the ash cloud in each image, as detected 
        by  APES or other method (km^2)
     'MERpl' - A vector of the mass eruption rate (MER) (continuous source)
        of the plume (kg/s)
     'MERpli' - A vector of estimated mass (instantaneous source)
        in the plume (kg)
     'MERpa' - A vector of the mass eruption rate (MER) (continuous source) 
        of ash particles (kg/s)
     'MERpai' - A vector of estimated mass of ash particles (instantaneous
        source) in the plume (kg) 
     'cloudtype' - A vector that gives a label for cloudtype; 
        cloudtype 1 = downwindplume, cloudtype 2 = umbrella cloud
     'MER_csv_file' - A filename for the .csv output

    Output:
     Writes out a csv file to the results folder, or that specified by 
		the output csv filename
    """

    # Pre-allocate space for the matrix of results
    matrix_of_results = np.zeros((len(tss),7))

    # Assign each column in the matrix to a different vector of values
    matrix_of_results[:,0] = tss
    matrix_of_results[:,1] = A
    matrix_of_results[:,2] = maxPh - Ph
    matrix_of_results[:,3] = rhobar - rhogas
    matrix_of_results[:,4] = MERpa
    matrix_of_results[:,5] = mass
    matrix_of_results[:,6] = cloudtype

    # Create the file that will be written to
    # Uses the original filename so that it wont be written over each time
    #f = open('MER_' + 'filename' + '.csv', 'w')
    f = open(MER_csv_file, 'w')
    writer = csv.writer(f)
    # Specify headers for the columns
    writer.writerow(['time(s)', 'Area (M^2)', 'Cloud depth, m', 'Particle field density, kg/cu m', 'MER ash particles (kg/s)', 'Cum. mass ash (kg)', 'cloudtype'])
    # Write about the values in the matrix, row-by-row
    for values in matrix_of_results:
        writer.writerow(values)
    f.close()


