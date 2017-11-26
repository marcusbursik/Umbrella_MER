"""
Name: power_fit_coeffs
Version: 0.3
Date: 24 November 2017
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu

"""

import sys
import numpy as np 						# numpy for array operations
import matplotlib.pyplot as plt			# use for plotting and figures
from scipy.optimize import curve_fit	# curve fitting
# import math								# math operations

# How to handle invalid value errors raised by power_func
np.seterr(invalid = 'ignore')

# Create an error for when the cloudtype changes more than once, 
#  from umbrella cloud <--> downwind plume
class CloudtypeError(Exception):
    pass

# Function to fit with x, y
def power_func(x_tss,c,a):
    return (c*x_tss)**a

def power_fit_coeffs(A,tss,cloudtype):
    """
    [ x_tss, y_A, popt, power_func, c, a ] = power_fit_coeffs(A,tss)

    Description: This function fits the area and time results to a power 
    law equation, y = cx^a. 'c' and 'a' are estimated. There is the option to 
     plot the points and the best fit line. 

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
	
    # x_tss is the time data, y_A is area data
    x_tss = tss
    y_A = A

    # Make sure data is float
    x_tss = np.array(x_tss, dtype=float)
    y_A = np.array(y_A, dtype=float)

    # Create an empty list for cloud change indices, that will be appended
	#  to if the cloudtype changes

    cloud_change = []
    
    for idx in range(0,len(cloudtype)):
        if idx == 0:
            continue
        else:
            if cloudtype[idx] - cloudtype[idx-1] != 0:
                cloud_change.append(idx)
            else:
                continue

	print 'cloud_change', cloud_change

	# If there is more than one index in the cloud_change list, this means
	#  that the cloudtype changed more than one time, which is 
	#  unphysical. If this is the case, an error is raised
    if len(cloud_change) > 1:
        raise CloudtypeError("The ash cloud in the images indicates more\
		  than one change of cloudtype from umbrella cloud <--> downwind\
		  plume. In the correct case, only one type of change, if any, is\
 		  expected: from umbrella cloud --> downwind plume.")

	# If the length of the cloud_change list is 0, the cloudtype 
	#  did not change, so fit the data with one best fit power law equation
    elif len(cloud_change) == 0:
        popt, pcov = curve_fit(power_func, x_tss, y_A)
        c = popt[0]
        a = popt[1]
        one_stdev_err = 100.*np.sqrt(np.diag(pcov))

	# Otherwise if the length of the cloud_change list is 1, there was one
	#  change in cloudtype. This is physical, and will create two fits
    else:
		# Pre-allocate space
        c = np.ones(2)
        a = np.ones(2)
        one_stdev_err = np.ones([2,2])
        
		# Fit the data with two best fit equations
        for idx in range(len(cloud_change)):
            if idx == 0:
                x_tss1 = x_tss[0:cloud_change[idx]]
                y_A1 = y_A[0:cloud_change[idx]]
                try:
                    popt1, pcov1 = curve_fit(power_func, x_tss1, y_A1)
                    c[0] = popt1[0]
                    a[0] = popt1[1]
                    one_stdev_err[0,:] = np.sqrt(np.diag(pcov1))
                except:
                    e = sys.exc_info()[0]
                    print "Error: %s" % e

                x_tss2 = x_tss[-(len(cloud_change)-cloud_change[idx]-1):]
                y_A2 = y_A[-(len(cloud_change)-cloud_change[idx]-1):]
                try:
                    popt2, pcov2 = curve_fit(power_func, x_tss2, y_A2)
                    c[1] = popt2[0]
                    a[1] = popt2[1]
                    one_stdev_err[1,:] = np.sqrt(np.diag(pcov2))
                except:
                    e = sys.exc_info()[0]
                    print "Error: %s" % e

    # Now plot!

    plt.plot(x_tss, y_A, 'ro', label="Original Data")

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
        plt.plot(x_tss, power_func(x_tss, *popt), label="Fitted Curve")

	# Otherwise if the length of the cloud_change list is 1, there was one
	#  change in cloudtype. This is possible, and we will plot two fits 
    else:
        # Plot the first best fit function
        plt.plot(x_tss1, power_func(x_tss1, *popt1), label="Fitted Curve 1")

        # Plot the second best fit function
        plt.plot(x_tss2, power_func(x_tss2, *popt2), label="Fitted Curve 2")

    plt.xlabel('Time (s)')
    plt.ylabel('Area (m^2)')
    plt.title('Time vs. Area with Fitted Power Curve')

    return x_tss, y_A, power_func, c, a, one_stdev_err
