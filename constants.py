"""
To use:
    add `from constants import *` to header
"""


# Physical Constants
GRAVITATIONAL_CONSTANT = 6.67 * 10**-11
MASS_EARTH = 5.9724 * 10**24  # kg
MASS_MARS = 0.64171 * 10**24  # kg
RADIUS_EARTH = 6.378 * 10**6  # m
AU = 146230000000 #m

# Rocket Constants
# Source: https://www.spacex.com/sites/spacex/files/making_life_multiplanetary-2017.pdf
MASS_FUEL = 9.98 * 10**5  # kg
MASS_ROCKET = 77.111 * 10**3  # kg
ORTH_SURFACE_AREA = 3.1415 * 4.5**2  # m^2
DRAG_COEFF = 0.25  # Rough estimate from research
