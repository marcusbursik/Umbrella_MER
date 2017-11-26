Version: 0.4
Date: 26 November 2017
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

To run the functions to calculate and display measured cloud diameters:
>>> python main_diameters.py

All files needed, other than python modules, are contained in the test folder. These do 
not need to be moved to the src folder to run main_cloudtype and main_diameters.  
Among the files in the test folder at present, is "testfull2.txt", which contains all 
the satellite and meteorological data 
needed to calculate MER.  These data are currently derived from the APES algorithm, the 
main_diameters module contained herein, and "by hand" from other meteorologic or satellite 
data.

All results files are saved in the results folder. 
