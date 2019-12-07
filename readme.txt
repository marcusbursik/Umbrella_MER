Version: 0.5.1
Date: 6 December 2019
Coding: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu

INTRODUCTION
This software is written to estimate mass eruption rate, or mass flux of ash into ash cloud
given a sequence of satellite images in which the ash cloud objects have been identified.
See version.txt for information on current status of version.  Built in Anaconda python 2.7; 
needs scipy, numpy and cv2 (image processing).  See build_environment.txt for (at least) the
initial build environment.

RUNNING
To run the programs, you must be in the src directory. 

To run the modules to estimate MER, and estimate cloud flow regime (umbrella or downwind):
>>> python main_cloudtype.py

To run the functions to calculate and display measured cloud diameters:
>>> python main_diameters.py

All files needed for input are contained in the test folder. These do 
not need to be moved to the src folder to run main_cloudtype and main_diameters.  

Among the files in the test folder are “test_tinakula_1_ftc.ssv” and "data_manam_2015_ftc.ssv", which contain all the satellite and meteorological data needed to calculate MER for the 20 October 2017 eruption of Tinakula, Solomon Islands, and the 20 October 2015 eruption of Manam, PNG.  These data could be derived from the APES, COTAC or VOLCAT algorithm, the main_diameters module contained herein, or "by hand" from meteorologic or satellite data. The Tinakula example data were all derived from COTAC; Manam "by hand". 
 
All results files from running a test for either Tinakula or Manam are saved in the results folder. 

In normal operation, separate "input" and "output" folders can be made, and used and referenced to in main_cloudtype or main_diameters.

THE INPUT FILE
The example input file names contain the string "ftc" because input data for height are in ft, and for temperature are in celsius.  This is an artifact of the set up of Visual Weather at VAAC Darwin, but is also useful for aviation.

Note that a start file can also be provided, if there is evidence of start time aside from satellite imagery.  The one in the "test" directory is for Manam.  It contains one number, the start time of the eruption, in the same format used in the main input file.

The input file is a "space separated value" file (.ssv).  A "comma separated value" file (.csv), which can be output directly from Excel could also be used, and a universal find/replace done on "comma".
  
The units for the input variables are (screen name at Darwin VAAC then python name; arrow indicates change in program to calculated units):
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
‘PIE’       'P0' - Vector of pressure at that height, from sounding (input hPa -> Pa)
‘HCT’       'maxPh' - Vector of maximum plume height at which T = maxt (input ft -> m) 
‘BTCT’      'maxt' - Vector of brightness temperature at maximum plume height (input C -> K)
‘PCT’       'Pp' - Vector of pressure of plume at maxPh from sounding (input hPa -> Pa)
‘HW’        'Z' - Vector of height at which windspeed is known (input ft -> m)
‘WK’        'uk' - Vector of wind speed in knots at Z (knots)
——          'u' - Vector of wind speed in m/s at Z (m/s)
