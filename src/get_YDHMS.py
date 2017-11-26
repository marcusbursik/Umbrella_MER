"""
Name: get_YDHMS
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import numpy as np			# numpy for array operations

def get_YDHMS(treal_string, start_filename):
    """
    [Y, D, H, M, S, Y0, D0, H0, M0, S0] = get_YDHMS(treal_string, start_filename)

    Description: This function separates the string of time formatted 
     data to get data for YYYY, DDD, HH, MM, SS

    Input:
     'treal_string' - A string of the time the image was taken, preserves 
       '0' characters (YYYYDDDHHMMSS)
     'start_filename' - A .txt file with the start time of the eruption 
        in the format ?YYDDDHHMMSS. If start_filename == 'None', the 
        start time of the eruption is assumed to be the time that the 
        original image was taken

    Output:
     'Y' - A vector of the year each image was taken
     'D' - A vector of the day of the year each image was taken (1-366)
     'H' - A vector of the hour each image was taken (0-23)
     'M' - A vector of the minute each image was taken (0-59)
     'S' - A vector of the second each image was taken (0-59)
     'Y0' - The start year of the eruption
     'D0' - The start day of the eruption
     'H0' - The start hour of the eruption
     'M0' - The start minute of the eruption
     'S0' - The start second of the eruption
    """
    # Pre-allocate space for each vector
    # Pre-allocare space for the year vector
    Y = np.zeros(len(treal_string))
    # Pre-allocare space for the day vector
    D = np.zeros(len(treal_string))
    # Pre-allocare space for the hour vector
    H = np.zeros(len(treal_string))
    # Pre-allocare space for the minute vector
    M = np.zeros(len(treal_string))
    # Pre-allocare space for the second vector
    S = np.zeros(len(treal_string))

    # Index through each element of 'treal_string' to get info
    for index in range(0,len(treal_string)):
        current_treal = treal_string[index]
        Y[index] = float(current_treal[1:3])    # Gets the year 
        D[index] = float(current_treal[3:6])    # Gets the day
        H[index] = float(current_treal[6:8])    # Gets the hour
        M[index] = float(current_treal[8:10])   # Gets the minute
        S[index] = float(current_treal[10:12])	# Gets the second

    # If no start filename is specified with a separate eruption start time,
    #  the eruption start time is assigned to the time that the first image
	#  was taken.
    if start_filename == 'None':
        Y0 = Y[0]
        D0 = D[0]
        H0 = H[0]
        M0 = M[0]
        S0 = S[0]

	# Otherwise, get the information from an alternate start time 
	#  from a text file that contains only the start time in the 
	#  format ?YYDDDHHMMSS.
    else:
		# Open the start filename file for reading
        f = open(start_filename, 'r')
		# Read the file
        start_time = f.read()
        # Close the file
        f.close()

        Y0 = float(start_time[1:3])     	# Gets the start year
        D0 = float(start_time[3:6])     	# Gets the start day
        H0 = float(start_time[6:8])     	# Gets the start hour
        M0 = float(start_time[8:10])        # Gets the start minute
        S0 = float(start_time[10:12])       # Gets the start second

    return Y, D, H, M, S, Y0, D0, H0, M0, S0
