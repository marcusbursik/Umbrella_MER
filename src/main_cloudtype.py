"""
Name: main_cloudtype
Description: Wrapper program to get data and calculate mass eruption rate (MER) for a growing volcanic cloud.
Version: 0.4
Date: 23 November 2017
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

# Import python libraries
import sys,os
import matplotlib.pyplot as plt
import math
import numpy as np
import csv
from scipy.optimize import curve_fit
from scipy import stats
import scipy

# Import modules in the src directory
from get_MERs_cloudtype import *
from get_N import *
from get_YODHMS import *
from get_info_from_txt import *
from get_rhos import *
from get_tss import *
from plot_MER import *
from plot_tss_vs_A import *
from power_fit_coeffs import *
from get_probabilities import *
from write_MER_data import *

if __name__ == '__main__':

    # Define the current path
    path = os.getcwd()

    # Specify the needed input filenames

    # Filename containing majority of data
    data_filename = path[:-4] + '/test/' + 'data_manam_2015_ftc.ssv'

    # Filename containing the start time of the eruption, in form ?YYDDDMMHHSS
    start_filename = 'None'
       # start_filename = path[:-4] + '/test/' + 'start_downwind.txt'

    
    # Specify the needed output filenames

    # Filename to store probability data
    probabilities_txt_filename  = path[:-4] + '/results/' + 'probabilities.txt'

    # Filename to store MER data
    MER_csv_file = path[:-4] + '/results/' + 'MER_data.csv'


    # Get info from txt
    [ treal_string, treal, A, D1, D2, Ph, Tb, P0, maxPh, maxT, Pp, Z, uk, u] = get_info_from_txt(data_filename, delimeter=' ')

    # Get YODHMS
    [ Y, O, D, H, M, S, Y0, O0, D0, H0, M0, S0] = get_YODHMS(treal_string, start_filename)

    # Get tss
    tss = get_tss(Y, O, D, H, M, S, Y0, O0, D0, H0, M0, S0)

    # Get rhos
    [ rhobar, rhogas] = get_rhos(P0, Pp, maxT, Tb, Rd = 287.)

    # Get N
    N = get_N(Tb, maxT, Ph, maxPh, g = -9.81)

    # Get MERs and cloudtype
    [ L, MERpl, MERpli, MERpa, MERpai, cloudtype, mass ] = get_MERs_cloudtype( D1, D2, rhobar, tss, A, N, u, rhogas)

    # Write out MER data
    write_MER_data(tss, A, maxPh, Ph, rhobar, rhogas, MERpa, mass, cloudtype, MER_csv_file)

    # Plot Time vs. Area
    plot_tss_vs_A(tss, A, L, N, u, rhobar)

    # Get power function coefficients 
    [ x_tss, y_A, power_func, c, a, one_stdev_err ] = power_fit_coeffs(A,tss,cloudtype)
    # And best-fit power functions
    get_probabilities(c, a, one_stdev_err, probabilities_txt_filename)

    # Plot time vs. MER
    # plotMER(MERpl, tss, 'Time(s)', 'MER of cloud (kg/s)', 'Time vs. MER of cloud')
    # plotMER(MERpli, tss, 'Time(s)', 'Mass of puff, instantaneous source (kg)', 'Time vs. Estimated mass of puff')
    plotMER(MERpa, tss, 'Time(s)', 'MER of particles (kg/s)', 'Time vs. MER of particles')
    plotMER(mass, tss, 'Time(s)', 'Cum. mass of particles (kg)', 'Time vs. Mass of particles')


