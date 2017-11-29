"""
Name: main_diameters
Description: Wrapper program to get diameters/radii across clouds from images.
Version: 0.4
Date: 27 November 2017
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

# Import python libraries
import sys
import numpy as np
import cv2
import math
from scipy import ndimage
import os
import csv

# Import modules from src directory
from contours_com import *
from get_radii import *
from get_diameters import *
from write_diameter_data import *

# I think it's good to declare this globally
# who knows where it could be needed
km_per_pixel = 4.75

if __name__ == '__main__':

    # Define the current path
    path = os.getcwd()
    
    # Specify the needed output filenames
    diameters_csv_file = path[:-4] + '/results/' + 'diameters.csv'

    # Define the path for the input test files
    path_test = path[:-4] + '/test'

    # Determine which test images should be used as cloud masks
    files = [f for f in os.listdir(path_test) if f.startswith('test_cloud')]

    # Pre-allocate space for diameter vectors
    area = np.zeros(len(files))
    D1 = np.zeros(len(files))
    D2 = np.zeros(len(files))

    # Go through each cloud mask image
    count=0
    for index in range(0,len(files)):
        # Get the filename with extension
        filename = path_test + '/' + files[index]
        # Heading is filename without extension
        heading = files[index]
        heading = heading[0:12]
        # read in image of cloud mask
        im = cv2.imread(filename)

        # Get the contours, area and center of mass coordinates
        contours, x_com, y_com, img, area[index] = contours_com(im)
        area[index] = area[index] * km_per_pixel * km_per_pixel

        # Get every radius in cloud mask from contour to center of mass
        radii, cur_x0, cur_y0 = get_radii(contours, x_com, y_com)

        # Get the maximum and minimum diameters in the cloud mask
        D1[index], D2[index] = get_diameters(count,contours, img, x_com, y_com, radii, cur_x0, cur_y0, km_per_pixel)
        count = count+1

        # Write out img with contours and center of mass drawn on
        cv2.imwrite(path[:-4] + '/results/' + 'contours_COM_' + files[index], im)
        
    write_diameter_data(area, D1, D2, diameters_csv_file)
