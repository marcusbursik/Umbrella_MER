#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 11:20:33 2017

@author: mib
"""

def plot_power_fit(x_tss, y_A, c, a):
    """
    plot of A v. time with power fits = plot_power_fit(x_tss, y_A, c, a)

    Description: This function uses fits of area and time results to a power 
    law equation, y = cx^a. 'c' and 'a' are estimated in power_fit_coeffs(). 
    This plots the points, the best fit line and the best integer ratio fit
    from get_probabilities(). 

    Input:
     'A' - Vector of area of the ash cloud in each image, as detected 
        by a previous algorithm (km^2) 
     'tss' - Vector of number of seconds since the eruption, assuming 
        that the eruption occured at the time that the first image in 
        the file was taken

    Output:
     'x_tss' - Vector of floats of the seconds since the start of 
		the eruption
     'y_A' - Vector of floats of the area of the ash cloud in each 
		image, as detected by a previous algorithm (km^2)
     'popt' - Vector of the constant variables found from the regression
     'power_func' - The function with constants to be fit
     'c' - The constant in y = cx^a
     'a' - The power constant in y = cx^a
	  
	 -- plot of fit and data is also an output figure -- 
    """
	
     # Plot the power fit, and best coefficients

    plt.loglog(x_tss, y_A, 'b*', label="Data")
    strformat = 'a: {0:.3f}'
    fmt = '{0:.2f}'

	# If there is more than one index in the cloud_change list, this means
	#  that the cloudtype changed more than one time, which is not 
	#  physical. If this is the case, an error is raised
    if len(cloud_change) > 1:
        raise CloudtypeError("The ash cloud in the images indicates more\
		  than one change of cloudtype from umbrella cloud <--> downwind\
 		  plume. Physically, only one type of change, if any,\
		  is expected: from umbrella cloud --> downwind plume.")

	# If the length of the cloud_change list is 0, the cloudtype 
	#  did not change, so plot the fitted function, when only one 
	#  fit was needed
    elif len(cloud_change) == 0:
        plt.loglog(x_tss, power_func(x_tss, *popt), label=strformat.format(a))

	# Otherwise if the length of the cloud_change list is 1, there was one
	#  change in cloudtype. This is possible, and we will plot two fits 
    else:
        # Plot the first best fit function
        plt.loglog(x_tss1, power_func(x_tss1, *popt1), label=strformat.format(a[0]))

        # Plot the second best fit function
        plt.loglog(x_tss2, power_func(x_tss2, *popt2), label=strformat.format(a[1]))

    plt.xlabel('Time (s)')
    plt.ylabel('Area (m^2)')
    plt.legend(loc = 'lower right', title = 'area=c*time^a')
    plt.title('Time vs. Area with Fitted Power Curve')
