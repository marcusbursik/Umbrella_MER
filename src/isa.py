"""
    Module to compute ICAO/ISA standard atmosphere
    From isa.py at https://gist.github.com/buzzerrookie/
    Downloaded: 30 November 2017
    No known license
    Pressure in Pa, temperature in K, density in kg/cu m and height in m 
    Given that we are getting pressure, height, density = isa(temperature),
    This only works for ICAO troposphere, below 11 km
    M. Bursik 1 Dec 2017
"""    

import sys
import math

g = 9.80665
R = 287.00
def cal(p0, t0, a, h0, t1):
    if a != 0:
        # t1 = t0 + a * (h1 - h0)
        h1 = (t1 - t0)/a + h0
        p1 = p0 * (t1 / t0) ** (-g / a / R)
    else:
        h1 = R * t1 / g
        p1 = p0 * math.exp(- g * h1 / R / t0)
    return h1, p1

def isa(temperature):
    a = [-0.0065, 0, 0.001, 0.0028]
    t = [216.65, 216.65, 228.65, 270.65]
    p0 = 108900.0   #These values from wikipedia, noting that ISA starts at h0 = -611.0
    t0 = 292.15
    h0 = -610.0
    if temperature < t[0] or temperature > t0:
        print("temperature must be in [217, 292]. suspect rapid rise/undercooling.")
        return

    else:
        altitude, pressure = cal(p0, t0, a[0], h0, temperature)
        density = pressure / (R * temperature)
        strformat = 'Temperature: {0:.2f} \nPressure: {1:.2f} \nAltitude: {2:.4f} \nDensity: {3:.4f}'
        print(strformat.format(temperature, pressure, altitude, density))
        return temperature, pressure, altitude, density

if __name__ == '__main__':
    # command line option
    if len(sys.argv) != 2:
        print("Usage: ./isa.py <temperature>")
        sys.exit(-1)
    try:
        temperature = float(sys.argv[1])
    except:
        print("Wrong temperature format!")
        sys.exit(-2)
    isa(temperature)
