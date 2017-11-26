"""
Name: get_rhos
Version: 0.1
Date: 11 August 2015
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu

"""

def get_rhos(Pp, Vt, Tb, Rd = 287, k = 2./7., P0 = 1000, g = -9.81):
    """
    [ T, rhobar, rhogas] = get_rhos_N(Pp, Vt, Tb, Rd = 287, k = 2./7., P0 = 1000, g = -9.81)

    Description: This function takes in parameters to calculate the 
     plume density at the neutral buoyancy height, 
     and the density of the gas in the cloud. See Pouget et al. (2013, JVGR).

    Input:
     'Pp' - Vector of pressure of plume at height Ph, near the level of 
        neutral buoyancy, from NWP, radiosonde, etc. (hpa)
     'Vt' - Vector of virtual potential temperature in each image (K)
     'Tb' - Vector of plume spreading temperature at the level of neutral 
        buoyancy, "brightness temperature" in each image (K)
     'Rd' - Gas constant for dry air = 287 (J/K/Kg) unless noted otherwise
     'k' -  Constant = 2./7. unless noted otherwise
     'P0' - Sea level standard atmospheric pressure = 1000 (hPa) unless 
        noted otherwise
     'g' - Constant of gravity = -9.81 (m/(s^2)) unless noted otherwise

    Output:
     'T' - Temperature at the neutral buoyancy height
     'rhobar' - Plume density at the neutral buoyancy height
     'rhogas' - The density of the gas at neutral buoyancy height
    """

    # Define absolute temperature from virtual temperature
    T = ((Pp/P0) ** k) * Vt
    # Calculate rhobar
    rhobar = Pp / (T * Rd)
    # Calculate rhogas
    rhogas = Pp / (Tb * Rd)

    return T, rhobar, rhogas
