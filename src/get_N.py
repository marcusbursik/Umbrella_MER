"""
Name: get_N
Version: 0.4
Date: 07 December 2017
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu

"""

import numpy as np				# numpy for array operations

def get_N(Tb, maxT, Ph, maxPh, g = -9.81):
    """
    N = get_N(PTb, maxT, Ph, maxPh, g = -9.81)

    Description: This function calculates the buoyancy frequency. 

    Input:
     'Tb' - Vector of brightness temperature max *outer edge* (K)
     'maxT' - Vector of temperature at maximum plume height in each image (K)
     'Ph' - Vector of plume spreading height at the level of neutral 
        buoyancy in each image (m)
     'maxPh' - Vector of maximum plume height in each image (m)
     'g' - Constant of gravity = -9.81 (m/(s^2)) unless noted otherwise

    Output:
     'N' - The buoyancy frequency, assuming the min height of plume is Ph, 
        min temp of plume is maxT 
    """

    # Calculate N
    if (maxT.any() - Tb.any()) > 0:
        N = np.sqrt(-(g/Tb) * ((maxT - Tb) / (maxPh - Ph)))
    else:
        N = np.full(shape=len(Tb), fill_value=0.035, dtype=float)

    return N
