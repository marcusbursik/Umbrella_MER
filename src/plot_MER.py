"""
Name:
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import matplotlib.pyplot as plt 	# use for plotting and figures

def plotMER(MER, tss, x_label='Time(s)', y_label='MER_type', title='Time vs. MER'):
    """
    plot of Time vs. MER =  plotMER(MER, tss, x_label='Time(s)', y_label, title): 

    Description: Plots the time vs. MER  or estimated mass data.

    Input:
     'MER' - Vector of mass eruption rates (or est. mass) with change in time interval
     'tss' - Vector of number of seconds since eruption start 
     'x_label' - The x-axis label of the plot, representing the time since 
        the start of the eruption in seconds(s)
     'y_label' - The y-axis label of the plot, representing the MER ((m^3)/s) 
     'title' - The title of the plot

    Output: 
     plot of Time vs. MER
    """
    # Plot MER data
    fig = plt.figure()
    plt.plot(tss, MER, 'ro')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
