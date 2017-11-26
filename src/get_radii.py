"""
Name: get_radii
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import numpy as np			# numpy for array operations

def get_radii(contours, x_com, y_com):
	"""
	[ radii, cur_x0, cur_y0 ] = get_radii(contours, x_com, y_com)

	Description: This function gets all radii by calculating Euclidean
	 distance from the x,y center of mass coordinate to the coordinates of
	 each contour. It also returns the x,y coordinates of the contours as
	 if the center of mass coordinate was at an origin (0,0) point
	
	Input:
	 'contours' - an array of image contour pixel locations 
	 'x_com' - the x-coordinate pixel location for the center of mass
	 'y_com' - the y-coordinate pixel location for the center of mass

	Output:
	 'radii' - A vector of radii that describe each radius from the center
		of mass of an object to the contour pixel locations on an image
		of a cloud mask
	 'cur_x0' - A vector of the x locations of each contour pixel, with 
		respect to the center of mass pixel location as the origin 
	 'cur_y0' - A vector of the y locations of each contour pixel, with
		respect to the center of mass pixel location as the origin 
	"""
	# Get the shape of contours to determine how much space to pre-allocate
	r, c = contours.shape
    
	# Pre-allocate space
	cur_x = np.zeros(r)
	cur_y = np.zeros(r)
	radii = np.zeros(r)

	# Get radius for each contour coordinate 
	for curRow in range(0, r): 
		cur_row = contours[curRow, :]
		cur_x[curRow] = cur_row[0]
		cur_y[curRow] = cur_row[1]
    
		# Use Euclidean distance equation to get radius distance
		radii[curRow] = np.sqrt((x_com - cur_x[curRow])**2 + (y_com - cur_y[curRow])**2)

	# Get x,y locations with respect to the center of mass as 
	#  an origin point (0,0)
	cur_x0 = cur_x - x_com
	cur_y0 = cur_y - y_com
	
	return radii, cur_x0, cur_y0
