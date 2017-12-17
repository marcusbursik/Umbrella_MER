"""
Name: get_tss
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import numpy as np			# numpy for array operations

def get_tss(Y, O, D, H, M, S, Y0, O0, D0, H0, M0, S0):
    """
    def get_tss(Y, O, D, H, M, S, Y0, O0, D0, H0, M0, S0): tss = get_tss(Y, O, D, H, M, S, Y0, D0, H0, M0, S0)

    Description: This function gets the time in seconds from the beginning 
     of the eruption.
     
     The beginning of the eruption is assumed to be the time that 
     the original image was taken, unless there is a start file with
     a start time derived from different data.

    Input:
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

    Output:
     'tss' - A vector of number of seconds since the eruption, assuming 
       that the eruption started at the time that the first image in 
       the file was taken, or at the time given in the start file
    """

    # Pre-allocate space for tss
    tss = np.zeros(len(Y))

    for i in range(0,len(Y)):

    # Assume that change is no greater than 1 year
    # 3600 sec/hour, 60 min/hour, 60 sec/min

        if Y0 != Y[i]:
        # Indicates different year
            if Y0%4 == 0:
            # Use modulus division to consider leap years
                n = 366. - D0 + D[i] - 2.
            else:
            # For regular years (?? Math works out to the the same?)
                n = 365. - D0 + D[i] - 1.
            tss[i] = (((24. - H0 + H[i] - 1) + (24.*n)) * 3600.) + ((60. - M0 + M[i] - 1) * 60.) + (60. - S0 + S[i])

        elif D0 < D[i]:
        # Same year, different day
            n = D[i] - D0 - 1
            tss[i] = (((24. - H0 + H[i] - 1) + (24. * n)) * 3600.) + ((60. - M0 + M[i] - 1) * 60.) + (60. - S0 + S[i])

        elif H0 < H[i]:
        # Same year, same day, different hour
            tss[i] = ((H[i] - H0 - 1) * 3600.) + ((60. - M0 + M[i] - 1) * 60.) + (60. - S0 + S[i])

        elif M0 < M[i]:
        # Same year, same day, same hour, different minute
            tss[i] = ((M[i] - M0 - 1) * 60.) + (60. - S0 + S[i])

        elif S0 < S[i]:
        # Same year, same day, same hour, same minute, different second
            tss[i] = S[i] - S0

        else:
        # All same
            tss[i] = 0

    return tss

