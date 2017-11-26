"""
Name: plot_tss_vs_A
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import matplotlib.pyplot as plt 	# use for plotting and figures
import math							# math operations
import numpy as np					# numpy for array operations

def plot_tss_vs_A(tss, A, L, N, u, rhobar):
    """
    plot of Time vs. Area = plot_tss_vs_A(tss, A, L, N, u, rhobar)

    Description: This function plots Time vs. Area for theoretical
      relation and data. Theoretical curve is plotted with dashed, 
      colored lines. Data are plotted as a star and solid black line.  
    
    Input:
     'tss' - Vector of number of seconds since the eruption, assuming 
        that the eruption occured at the time that the first image in 
        the file was taken 
     'A' - Vector of area of the ash cloud in each image, as detected 
        by a previous algorithm (km^2) 
     'L' - A vector of lambda values, describe shape factor
     'N' - The buoyancy frequency, assuming the min height of plume is Ph, 
        min temp of plume is Vt 
     'u' - Vector of wind speed in m/s in each image (m/s) 
     'rhobar' - Plume density at height and temperature of the plume 
        at neutral buoyancy, Eqn. (4) in April 2013 paper

	Output:
	 plot of Time vs. Area 
    """

    # Define the theoretical time, in seconds
    theor_time1 = [10., 100.]
    theor_time2 = np.arange(1000,43000,2000)
    # Concatenate the two vectors into one vector of times
    theor_time = np.concatenate([theor_time1,theor_time2])

    # Pre-allocate space for the theoretical area vectors
    theor_A_dwp = np.zeros([9,len(theor_time)]) # Downwind plume
    theor_A_umb = np.zeros([9,len(theor_time)]) # Umbrella cloud

    # Get theoretical curves for time vs. Area 
    for log_index in range(0,9):
        for time_index in range(0,len(theor_time)):
            # An inverted Eqn. (9) from the unfinished paper, 
			#  solving for the area given a time
            theor_A_dwp[log_index,time_index] = 0.00001*(math.sqrt(((10.**(log_index+2.)) * 8. * L[0] * N[0] * (theor_time[time_index]**3.) * u[0]) / (9.*rhobar[0])))
            # An inverted Eqn. (6) from the unfinished paper, 
			#  solving for the area given a time
            theor_A_umb[log_index,time_index] = 0.00001*((((10.**(log_index+2.)) * 3. * math.sqrt(math.pi) * L[0] * N[0] * (theor_time[time_index]**2.)) / (2. * rhobar[0]))**(2./3.))

    # Plot theoretical curves / data curves for dwp
    fig = plt.figure()
    
	# Plot theoretical curves
    for index in range(0,len(theor_A_dwp[:,0])):
        plt.loglog(theor_time, theor_A_dwp[index,:], linestyle = 'dashed')
    
	# Plot data
    plt.loglog(tss, A, linestyle = 'solid', color = 'black')
    plt.loglog(tss, A, "b*")
    plt.xlabel('Time (s)')
    plt.ylabel('Area (km^2)')
    plt.title('Time vs. Area for Downwind Plume')
    plt.show()

    # Plot theoretical curves / data curves for umb
    fig = plt.figure()
    
	# Plot theoretical curves
    for index in range(0,len(theor_A_umb[:,0])):
        plt.loglog(theor_time, theor_A_umb[index,:], linestyle = 'dashed')
    
	# Plot data
    plt.loglog(tss, A, linestyle = 'solid', color = 'black')
    plt.loglog(tss, A, "b*")
    plt.xlabel('Time (s)')
    plt.ylabel('Area (km^2)')
    plt.title('Time vs. Area for Umbrella Cloud')
    plt.show()
