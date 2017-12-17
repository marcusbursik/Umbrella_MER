"""
Name: get_MERs_cloudtype
Version: 0.5
Date: 15 December 2017
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""

import numpy as np			# numpy for array operations
import math					# math operations


class MER_Error(Exception):
    pass

def get_MERs_cloudtype(D1, D2, rhobar, tss, A, N, u, rhogas):
    """ 
    Description: This function gets the mass eruption rates for 
    the identified cloudtype (umbrella cloud or downwind plume). 
    In the umbrella cloud case, MER is calculated assuming
    continuous emission, and mass is calculated in the case of
    an instantaneous emplacement.

    Use:
    [ L, MERpl, MERpli, MERpa, MERpai, cloudtype, mass] = \
    get_MERs_cloudtype( D1, D2, rhobar, tss, A, u, rhogas)

    Input: 
     'D1' - Vector of diameter measurement of the ash cloud in 
        each image (km)
     'D2' - Vector of diameter measurement of the ash cloud in 
        each image (km)
     'rhobar' - Plume density at height and temperature of the plume 
        at neutral buoyancy, Eqn. (4) in April 2013 paper
     'tss' - Vector of number of seconds since the eruption, assuming 
        that the eruption occured at the time that the first image in 
        the file was taken
     'A' - Vector of area of the ash cloud in each image, as detected 
        by a previous algorithm (km^2)
     'N' - The buoyancy frequency, assuming the min height of plume is Ph, 
        min temp of plume is Vt 
     'u' - Vector of wind speed in m/s in each image (m/s)
     'rhogas' - The density of the gas in the ash cloud, 
        Eqn. (13) in April 2013 paper

    Output:
     'L' - A vector of lambda values, describe shape factor 
     'MERpl' - A vector of the continuous mass eruption rate (MER) of the 
        plume (kg/s)
     'MERpli' - A vector of the instantaneous mass eruption rate (MER) of 
        the plume (kg/s)
     'MERpa' - A vector of the continuous mass eruption rate (MER) of the 
        particles (kg/s)
     'MERpai' - A vector of the instantaneous mass eruption rate (MER) of 
        the particles (kg/s)
     'mass' - A vector of cumulative mass of particles up to the indicated time (kg)
     'cloudtype' - A vector that gives a label for cloudtype; 
        cloudtype 1 = downwindplume, cloudtype 2 = umbrella cloud
    """

    # Pre-allocate space for each vector
    cloudtype = np.zeros(len(D1))
    L = np.zeros(len(D1))
    MERpl = np.zeros(len(D1))
    MERpli = np.zeros(len(D1))
    MERpa = np.zeros(len(D1))
    MERpai = np.zeros(len(D1))
    mass = np.zeros(len(D1))

    # Go through each image
    print "  "
    print "xxxxxxxxxxxxxxxxxx Cloud growth xxxxxxxxxxxxxxxxxxxxxxxxx"
    for cur_img in range(0,len(D1)):

        # Use extracted diameters of the cloud to identify if the plume
        #  is a downwind plume or an umbrella cloud
        ratio = np.amax([D1[cur_img],D2[cur_img]])/np.min([D1[cur_img],D2[cur_img]])
        # DEBUG: print "A, D1, D2, ratio =  ", A[cur_img], D1[cur_img], D2[cur_img], ratio

        if (ratio > 3.):
            # Identify lambda value
            L[cur_img] = 0.845
            # Identify cloud type
            cloudtype[cur_img] = 1

            if cur_img == 0:
            # Do nothing with MER because no previous to compare 
			#  to get a rate
                continue

            else:
                # Calculate MER
                # MER of DWP, continuous release
                MERpl[cur_img] = ((9. * rhobar[cur_img]) / (8. * L[cur_img] * N[cur_img] * u[cur_img])) * \
                     (( (A[cur_img]*1000000.)**2 - (A[cur_img-1]*1000000.)**2) / (tss[cur_img]**3 - tss[cur_img-1]**3))

                if MERpl[cur_img] >= 0:
                    print "Cloud is spreading as a downwind plume."
 
                if MERpl[cur_img] < 0:
                    print "sgn(dA/dt) = -1 => Dissipating."
                    MERpl[cur_img] = np.nan

                # MER of particles into DWP, continuous release
                if rhobar[cur_img] > rhogas[cur_img]:
                    MERpa[cur_img] = MERpl[cur_img] * (1 - (rhogas[cur_img]/rhobar[cur_img]))
                    
                else:
                    MERpa[cur_img] = MERpl[cur_img]
                    
                if MERpa[cur_img] < 0:
                    MERpa[cur_img] = np.nan
                else:
                    print "Mass flux of ash into cloud = ", MERpa[cur_img], " kg/s"

        else:
            # Identify lambda value
            L[cur_img] = 1
            # Identify cloud type
            cloudtype[cur_img] = 2

            if cur_img == 0:
            # Do nothing with MER because no previous to compare 
			#  to get a rate
            # Replace the MER calculation with a method so that can call with correct parameters, 
            # even for cur_img == 0.
                continue

            else:
                # Cloud is spreading as an umbrella cloud
                # Calculate MER
                # MER of umbrella cloud, continuous release
                MERpl[cur_img] = ((2. * rhobar[cur_img]) / (3. * (math.sqrt(math.pi)) * L[cur_img] * N[cur_img])) * \
                  (((A[cur_img]*1000000.)**(3./2.) - (A[cur_img-1]*1000000.)**(3./2.)) / (tss[cur_img]**2 - tss[cur_img-1]**2))

                if MERpl[cur_img] >= 0:
                    print "Cloud is spreading as an umbrella cloud."

                if MERpl[cur_img] < 0:
                    print "sgn(dA/dt) = -1 => Cloud dissipating."
                    MERpl[cur_img] = np.nan

                # Mass of umbrella cloud assuming emission stopped
                MERpli[cur_img] = ((math.sqrt(math.pi) * rhobar[cur_img]) / (3. * L[cur_img] * N[cur_img])) * \
                  (((A[cur_img]*1000000.)**(3./2.) - (A[cur_img-1]*1000000.)**(3./2.)) / (tss[cur_img] - tss[cur_img-1]))

                if MERpli[cur_img] < 0:
                    MERpli[cur_img] = np.nan
                          
                # MER of particles into umbrella cloud, continuous release
                if rhobar[cur_img] > rhogas[cur_img]:
                    MERpa[cur_img] = MERpl[cur_img] * (1 - (rhogas[cur_img] / rhobar[cur_img]))
                else:
                    MERpa[cur_img] = MERpl[cur_img]


                if MERpa[cur_img] < 0:
                    MERpa[cur_img] = np.nan
                else:
                    print "Mass flux particles into cloud = ", MERpa[cur_img], " kg/s"
                        
                # Mass of particles in umbrella cloud, instantaneous release
                if rhobar[cur_img] > rhogas[cur_img]:
                    MERpai[cur_img] = MERpli[cur_img] * (1- (rhogas[cur_img] / rhobar[cur_img]))
                else:
                    MERpai[cur_img] = MERpli[cur_img]

                if MERpai[cur_img] < 0:
                    MERpai[cur_img] = np.nan

        if cur_img == 0:
            # Do nothing with MER because no previous to compare 
            # to get a rate
            continue
            
        else:
            mass_cur_img = MERpa[cur_img] * (tss[cur_img] - tss[cur_img - 1])
            mass[cur_img] = mass_cur_img + mass[cur_img - 1]


	# Define a *test* vector for cloudtype to test what happens 
	#  when it changes
    #cloudtype = np.array([1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2])

    print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    print " "
    print "****************** Summary information *******************"
    
    mean_MERp = np.nanmean(MERpa[1:len(MERpa)])
    if len(MERpa) >= 3:
        std_MERp = np.nanstd(MERpa)
    else:
        std_MERp = 0.0
    print "Tot. mass particles = ", int(np.max(mass)), " kg"
    print "Est. volume (DRE) = ", int(np.max(mass)) / 1000. / 1000000000., " cu km"
    print "MERp(t) = ", list(MERpa), " kg/s"
    print "mean MERp = ", int(mean_MERp), " +/- ", int(std_MERp), " kg/s "
    print "eruption duration = ", int(np.amin([tss[len(D1)-1],tss[np.argmax(mass)]])), " s" 
    print "**********************************************************"

    return L, MERpl, MERpli, MERpa, MERpai, cloudtype, mass

