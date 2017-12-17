"""
Name: get_rhos
Version: 0.41
Date: 07 December 2017
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu

"""

def get_rhos(P0,  Pp, maxT, Tb, Rd = 287.):
    """
    [ rhobar, rhogas] = get_rhos_N(P0, Pp, maxT, Tb, Rd = 287.)

    Description: This function takes in parameters to calculate the 
     plume density at the neutral buoyancy height, 
     and the density of the gas in the cloud. Modified from Pouget et al. (2013, JVGR).

    Input:
     'P0' - Vector of pressure of plume at neutral buoyancy height, Ph, 
     from NWP, radiosonde, etc. (hpa)
     'Pp' - Vector of pressure of plume at height maxPh, near the top
     of the cloud, from NWP, radiosonde, etc. (hpa)
     'maxT' - Vector of lowest temperature in each image inside plume, 
     brightness T (K)
     'Tb' - Vector of plume spreading temperature at the level of neutral 
        buoyancy, "brightness temperature" in each image (K)
     'Rd' - Gas constant for dry air = 287 (J/K/Kg) unless noted otherwise

    Output:
     'rhobar' - Plume density at the neutral buoyancy height
     'rhogas' - The density of the gas at neutral buoyancy height
    """

    # This version does a very straightforward estimate from measurements
    # Assumes brightness temperatures can be used directly
    # Calculate rhobar
    rhobar = P0 / (Tb * Rd)
    # Calculate rhogas
    rhogas = Pp / (maxT * Rd)

    print "------------------ Density check ------------------------"
    print "Estimated bulk density of cloud = ", rhobar
    print "Estimated gas density = ", rhogas    
    print "---------------------------------------------------------"
    return rhobar, rhogas
