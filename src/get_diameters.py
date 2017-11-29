"""
Name: get_diameters
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import sys				# for main path directory
import numpy as np		# numpy for array operations
import math				# math operations
import cv2				# image processing operations

def get_diameters(count,contours, im, x_com, y_com, radii, cur_x0, cur_y0, km_per_pixel):
	"""
        Description: This function gets the minimum and maximum diameters 
          from a set of radii to the center of mass of a volcanic cloud. It converts 
	  the diameters from pixels to km.

	[D1, D2] = get_diameters(radii, cur_x0, cur_y0, km_per_pixel)

	Input:
	 'count' - A constant integer that tells which iteration the main code is on
	 'contours' - an array of image contour pixel locations
	 'im' - the output image from "contours_com.py" with drawn contours and
		center of mass
	 'x_com' - the x-coordinate pixel location for the center of mass
	 'y_com' - the y-coordinate pixel location for the center of mass
	 'radii' - A vector of radii that describe each radius from the center
		of mass of an object to the contour pixel locations on an image
		of a cloud mask
	 'cur_x0' - A vector of the x locations of each contour pixel, with 
		respect to the center of mass pixel location as the origin
	 'cur_y0' - A vector of the y locations of each contour pixel, with
		respect to the center of mass pixel location as the origin
	 'km_per_pixel' = A conversion factor used to convert from number of 
		pixels to number of kilometers (km)
	
	Output:
	 'D1' - A vector of minimum diameters, in terms of kilometers (km) 
	 'D2' - A vector of maximum diameters, in terms of kilometers (km)
	"""

	# Pre-allocate space for vectors and arrays
	angle1 = np.zeros([len(radii), len(radii)])
	angle2 = np.zeros([len(radii), len(radii)])
	angle_diff = np.zeros([len(radii),len(radii)])

	# Go through each radius
	for cur_idx in range(0,len(radii)):
		# Set the current x1, y1 values for this round of the for loop
		x1 = cur_x0[cur_idx]
		y1 = cur_y0[cur_idx]
		
		# Calculate angle #1 from the origin to the x1, y1 point
		angle1[cur_idx,:] = np.rad2deg(math.atan2(y1,x1))

		# If angle #1 was calculated as a negative, add 360
		if angle1[cur_idx,0]<0:
			angle1[cur_idx,:] = angle1[cur_idx,:]+360
		

		# Calculate angle #2 for each radius corresponding to the first
		#  set of radii
		for iter_idx in range(0,len(radii)):
			# Set the current x2, y2 values for this round of the internal
			#  for loop
			x2 = cur_x0[iter_idx]
			y2 = cur_y0[iter_idx]

			# Calculate angle #2 from the origin to the x2, y2 point
			angle2[:,iter_idx] = np.rad2deg(math.atan2(y2,x2))

			# If angle #1 was calculated as a negative, add 360
			if angle2[0,iter_idx]<0:
				angle2[:,iter_idx] = angle2[:,iter_idx]+360
			

	# Calculate the difference between angle1 and angle 2. To get the angles
	#  with respect to difference from 180 degrees, subtract 180. 
	angle_diff = np.abs(np.abs(angle1-angle2)-180)
		
    # Pre-allocate space for vectors
	min_in_col = np.zeros(len(angle_diff[:,0]))
	min_idx    = np.zeros(len(angle_diff[:,0]))

	for curCol in range(0, len(angle_diff[:,0])):
        # Get the minimum difference from 180, which should be the closest
		#  to zero. 
		min_in_col[curCol] = np.min(angle_diff[:,curCol])
		# Get the index where the minimum difference is located
		min_idx[curCol] = np.argmin(angle_diff[:,curCol])
	
	# Pre-allocate space for vector of diameters
	diameters = np.zeros(len(min_idx))

	# For each radius, get the corresponding radius that goes through the 
	#  center of mass and completes the diameter
	for index in range(0, len(min_idx)):
		diameters[index] = radii[index] + radii[min_idx[index]]

	# D1 is the minimum diameter in the mass
	# D2 is the maximum diameter in the mass
    # Convert the diameters from pixel distances to km distances
	D1 = np.min(diameters) * km_per_pixel
	D2 = np.max(diameters) * km_per_pixel

	max_idx_diam = np.argmax(diameters)
	min_idx_diam = np.argmin(diameters)
	
	md = radii[max_idx_diam] + radii[min_idx[max_idx_diam]]
	md = md * km_per_pixel
	mdd = radii[min_idx_diam] + radii[min_idx[min_idx_diam]]
	mdd = mdd * km_per_pixel

	pt1md = tuple(contours[max_idx_diam, :])
	pt2md = tuple(contours[min_idx[max_idx_diam], :])

	pt1mdd = tuple(contours[min_idx_diam, :])
	pt2mdd = tuple(contours[min_idx[min_idx_diam], :])

	cv2.line(im, pt1md, (int(round(x_com)),int(round(y_com))), (0,255,0), thickness=1, lineType=8, shift=0) 
	cv2.line(im, pt2md, (int(round(x_com)), int(round(y_com))), (0,255,0), thickness=1, lineType=8, shift=0) 
	cv2.line(im, pt1mdd, (int(round(x_com)),int(round(y_com))), (255,0,0), thickness=1, lineType=8, shift=0)
	cv2.line(im, pt2mdd, (int(round(x_com)),int(round(y_com))), (255,0,0), thickness=1, lineType=8, shift=0)

	path = sys.path[0]
	cv2.imwrite(path[:-4] + '/results/' + 'drawn_diameters_' + str(count) + '.png', im)

	
	return D1, D2                                    
