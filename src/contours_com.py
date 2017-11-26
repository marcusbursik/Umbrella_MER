"""
Name: contours_com
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import cv2					# utilizes opencv for image processing
import numpy as np			# numpy for array operations
from scipy import ndimage	# includes center of mass function

def contours_com(im):
	"""
	[contours, x_com, y_com, im] = contours_com(im)

	Description: Finds the contour pixel locations of a cloud mask (0/255),
	 and the center of mass pixel location of the mask.  
	
	Input:
	 'im' - an array of the cloud mask, with values 0 and 255


	 'x_com' - the x-coordinate pixel location for the center of mass
	 'y_com' - the y-coordinate pixel location for the center of mass
	 'im' - the output image with drawn contours and center of mass
	"""
	# convert the image to grayscale
	imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
	# threshold the image (should be a black(0)/white(255) mask)
	ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
	# save a copy of the original thresholded image because the 
	#  findContours function alters the file
	orig_thresh = thresh.copy()

	# find the contours of the image mask, returns the coordinates of 
	#  contours in terms of pixel location
	# ORIG: image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	# draw contours on the original image and make contours red
	cv2.drawContours(im, contours, -1, (0,0,255), 3)
	contours = np.vstack(contours).squeeze()
	cv2.imshow("contours test",im)

	# get the center of mass (COM) coordinates
	com = ndimage.measurements.center_of_mass(orig_thresh) 
	x_com = com[1]
	y_com = com[0]

	# draw the center of mass on the image with a plus at the location
	im[y_com-2, x_com] = (0,0,255)
	im[y_com-1, x_com] = (0,0,255)
	im[y_com, x_com]   = (0,0,255)
	im[y_com+1, x_com] = (0,0,255)
	im[y_com+2, x_com] = (0,0,255)
	im[y_com, x_com-2] = (0,0,255)
	im[y_com, x_com-1] = (0,0,255)
	im[y_com, x_com+1] = (0,0,255)
	im[y_com, x_com+2] = (0,0,255)
	cv2.imshow("centroid test",im)

	return contours, x_com, y_com, im
	
