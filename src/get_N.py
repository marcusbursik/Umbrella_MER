"""
Name: get_N
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu

"""

import numpy as np				# numpy for array operations

def get_N(Pp, Vt, maxT, Ph, maxPh, k = 2./7., P0 = 1000, g = -9.81):
    """
    [ maxVt, N ] = get_N(Pp, Vt, maxT, Ph, maxPh, k = 2./7., P0 = 1000, g = -9.81)

    Description: This function calculates the buoyancy frequency. 

    Input:
     'Pp' - Vector of pressure of plume at plume height Ph, the level 
        of neutral buoyancy, in each image (hpa)
     'Vt' - Vector of virtual potential temperature in each image (K)
     'maxT' - Vector of maximum plume height temperature in each image (K)
     'Ph' - Vector of plume spreading height at the level of neutral 
        buoyancy in each image (m)
     'maxPh' - Vector of maximum plume height in each image (m)
     'k' -  Constant = 2./7. unless noted otherwise
     'P0' - Sea level standard atmospheric pressure = 1000 (hPa) unless 
        noted otherwise
     'g' - Constant of gravity = -9.81 (m/(s^2)) unless noted otherwise

    Output:
     'maxVt' - Vector of maximum virtual potential temperatures in 
        each image
     'N' - The buoyancy frequency, assuming the min height of plume is Ph, 
        min temp of plume is Vt 
    """

    # Calculate max virtual temperatures based on max absolute temperatures
    maxVt = maxT * (P0 / Pp) ** k
    # Calculate N
    N = np.sqrt(-(g/Vt) * ((maxVt - Vt) / (maxPh - Ph)))

    return maxVt, N
