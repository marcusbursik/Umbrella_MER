"""
Name: get_info_from_txt
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import numpy as np			# numpy for array operations

def get_info_from_txt(data_filename, delimeter = ' '):
    """
    [treal_string, treal, A, D1, D2, Ph, Tb, maxPh, maxT, Vt, Z, Pp, uk, u] = get_info_from_txt(data_filename, delimeter = ' ')
    
    Description: This function opens a text file to 
     get information from previous algorithms or from radionde data, 
     for MER estimation.
     
    Input:
     'data_filename' - A file with information on the volcanic ash cloud 
        and surrounding atmosphere.  Each record contains the ash cloud
        and weather data for a time at which an image was acquired.
     'delimeter' - Indicates field separation character. By default, 
        white space. If the input is a .csv file,
        the delimeter should be ',' a comma. In other cases, it may be a
        '\t', for tab.

    Output:
      'treal_string' - A string of the time the image was taken, 
        preserves '0' characters (YYYYDDDHHMMSS)
      'treal' - Vector of time at which each image was taken
        (will not follow format above bc float)
      'A' - Vector of area of the ash cloud in each image, as detected 
        by APES or otherwise (km^2)
      'D1' - Vector of diameter measurements of the ash cloud in each 
        image (km)
      'D2' - Vector of diameter measurements of the ash cloud in each 
        image (km)
      'Ph' - Vector of plume spreading height at the level of neutral 
        buoyancy  (m)
      'Tb' - Vector of plume spreading temperature at the level of neutral 
        buoyancy, "brightness temperature" in each image (K)
      'maxPh' - Vector of maximum plume height (m) 
      'maxt' - Vector of temperature at maximum plume height (K)
      'Vt' - Vector of virtual potential temperature at that height (K)
      'Z' - Vector of height at which pressure and windspeed are known (m)
      'Pp' - Vector of pressure of plume  at Z from NWP, radiosonde, etc.(hpa)
      'uk' - Vector of wind speed in knots at Z (knots)
      'u' - Vector of wind speed in m/s at Z (m/s)
    """
    # Open the text file and read each line into a string
    # Open file
    f = open(data_filename, 'r')
    # Read in each line of the file; each line is a string
    data_strings = f.readlines()
    # Get the number of data strings which will equal the number of rows in the .txt file
    nRows = len(data_strings)

    # Pre-allocate space for the data 
    data_matrix = np.zeros([nRows-1, 12], dtype=float)

    # Get the data from the data strings into a matrix of values
    treal_string = [] # begins a list for the treal_string
    for index in range(0,len(data_matrix)):
        # Do not count the first line of headers
        current_string = data_strings[index+1]
        # Search the current string for the index of the new line character
        newline_index = current_string.index('\n')
        # Get rid of the \n character in each string
        no_newline_string = current_string[0:newline_index]
        # Split the string at the spaces
        current_row = no_newline_string.split(delimeter)
        # Put the separated string into the current row of the data matrix
        data_matrix[index,:] = current_row
        # Append the first element of the current row (YYYYDDDHHMMSS) to treal_string
        treal_string.append(current_row[0])

    # Define each output for the function from the data in data_matrix
    treal = data_matrix[-15:,0]         # Time img was taken
    A =  data_matrix[-15:,1]            # Area of plume (km^2)
    D1 = data_matrix[-15:,2]            # Diameter 1 (km)
    D2 = data_matrix[-15:,3]            # Diameter 2 (km)
    Ph = data_matrix[-15:,4]            # Plume spreading height (m)
    Tb = data_matrix[-15:,5]            # Plume brightness temperature (K)
    maxPh = data_matrix[-15:,6]         # Max plume height (m)
    maxT = data_matrix[-15:, 7]         # Max plume temp at height maxPh (K)
    Vt = data_matrix[-15:,8]            # Virtual potential temp (K)
    Z = data_matrix[-15:,9]             # Altitude (m)
    Pp = data_matrix[-15:,10]           # Plume pressure (hPa)
    uk = data_matrix[-15:,11]           # Wind speed (knots)

    f.close()                           # close file

    u = uk * 514444./1000000.           # Wind speed (m/s)

    return treal_string, treal, A, D1, D2, Ph, Tb, maxPh, maxT, Vt, Z, Pp, uk, u
