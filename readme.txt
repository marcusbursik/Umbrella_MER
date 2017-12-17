Version: 0.5
Date: 16 December 2017
Coding: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu

This software is written to estimate mass eruption rate, or mass flux of ash into ash cloud
given a sequence of satellite images in which the ash cloud objects have been identified.
See version.txt for information on current status of version.  Built in Anaconda python 2.7; 
needs scipy, numpy and cv2 (image processing).  See build_environment.txt for (at least) the
initial build environment.

To run the programs, you must be in the src directory. 

To run the modules to estimate MER, and estimate cloud flow regime (umbrella or downwind):
>>> python main_cloudtype.py

To run the functions to calculate and display measured cloud diameters (not in Git repository):
>>> python main_diameters.py

All files needed, other than python modules, are contained in the test folder. These do 
not need to be moved to the src folder to run main_cloudtype and main_diameters.  
Among the files in the test folder at present, is “data_manam_2015_ftc.ssv”, which contains all the satellite and meteorological data needed to calculate MER for the 20 October 2015 eruption of Manam, PNG.  These data can be derived from the APES, COTAC or VOLCAT algorithm, the main_diameters module contained herein, and "by hand" from other meteorologic or satellite data. The Manam example data were all derived “by hand” from Visual Weather. 
 
All results files are saved in the results folder. 

The units for the input variables are (screen name at Darwin VAAC then python name):
‘Time’      'treal_string' - A string of the time the image was taken, 
        preserves '0' characters (YYYYOODDHHMMSS)
——    	    'treal' - Vector of time at which each image was taken
        (will not follow format above bc float)
‘Area’      'A' - Vector of area of ash cloud in each image, as detected 
        by forecaster, VOLCAT or COTAC or otherwise (km^2)
‘D1’        'D1' - Vector of long diameter measurements of the ash cloud in each 
        image (km)
‘D2’        'D2' - Vector of short, orthogonal diameter measurements of the ash 
        cloud in eachimage (km)
‘HIE’       'Ph' - Vector of plume spreading height at the level of neutral 
        buoyancy  (input ft -> m)
‘BTIE’      'Tb' - Vector of plume spreading temperature at the level of neutral 
        buoyancy, "brightness temperature" in each image (input C -> K)
‘PIE’       'P0' - Vector of pressure at that height, from sounding (hPa)
‘HCT’       'maxPh' - Vector of maximum plume height at which T = maxt (input ft -> m) 
‘BTCT’      'maxt' - Vector of brightness temperature at maximum plume height (input C -> K)
‘PCT’       'Pp' - Vector of pressure of plume at maxPh from sounding (hPa)
‘HW’        'Z' - Vector of height at which windspeed is known (input ft -> m)
‘WK’        'uk' - Vector of wind speed in knots at Z (knots)
——          'u' - Vector of wind speed in m/s at Z (m/s)
