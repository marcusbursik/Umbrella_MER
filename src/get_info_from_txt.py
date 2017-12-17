"""
Name: get_info_from_txt
Version: 0.41
Date: 07 December 2017
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import numpy as np			# numpy for array operations

def get_info_from_txt(data_filename, delimeter = ' '):
    """
    [treal_string, treal, A, D1, D2, Ph, Tb, P0, maxPh, maxT, Pp, Z, uk, u] = get_info_from_txt(data_filename, delimeter = ' ')
    
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
        preserves '0' characters (YYYYOODDHHMMSS)
      'treal' - Vector of time at which each image was taken
        (will not follow format above bc float)
      'A' - Vector of area of the ash cloud in each image, as detected 
        by forecaster or COTAC or otherwise (km^2)
      'D1' - Vector of long diameter measurements of the ash cloud in each 
        image (km)
      'D2' - Vector of short, orthogonal diameter measurements of the ash 
        cloud in eachimage (km)
      'Ph' - Vector of plume spreading height at the level of neutral 
        buoyancy  (m)
      'Tb' - Vector of plume spreading temperature at the level of neutral 
        buoyancy, "brightness temperature" in each image (K)
      'P0' - Vector of pressure at that height (K), from radiosonde, hPa
      'maxPh' - Vector of maximum plume height (m) 
      'maxt' - Vector of brightness temperature at maximum plume height (K)
      'Pp' - Vector of pressure of plume  at maxPh from NWP, radiosonde, etc.(hPa)
      'Z' - Vector of height at which windspeed is known (m)
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
    Ph = data_matrix[-15:,4] * 0.3048   # Plume spreading height (input ft -> m)
    Tb = data_matrix[-15:,5] + 273.15   # Plume brightness temperature (input C -> K)
    P0 = data_matrix[-15:,6]            # Pressure at height Ph (hPa)
    maxPh = data_matrix[-15:, 7] * 0.3048 # Max plume height where maxT (input ft -> m)
    maxT = data_matrix[-15:,8] + 273.15 # (Min) temp at maxPh (input C -> K)
    Pp = data_matrix[-15:,9]            # Pressure at maxPh (hPa)
    Z = data_matrix[-15:,10] * 0.3048   # Plume height where wind speed measured (input ft -> m)
    uk = data_matrix[-15:,11]           # Wind speed (knots)

    f.close()                           # close file

    # Legacy
    u = uk * 514444./1000000.           # Wind speed (m/s)

    # print treal_string, treal, A, D1, D2, Ph, Tb, P0, maxPh, maxT, Pp, Z, uk, u
    return treal_string, treal, A, D1, D2, Ph, Tb, P0, maxPh, maxT, Pp, Z, uk, u
