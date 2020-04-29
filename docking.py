#some code
import matplotlib.pyplot as plt
import numpy as np
import math
#from Inflight import *
from launch import *
from contants import *


# Parameters
r_init = 99*(10**6) # m distance away from planet during landing/docking stage ### Will have to change
v0 = -7*10**3 # initial velocity (m/s) ### Will have to change
m_mars = float(input("What it the mass of Mars?\n ____ x 10^23> ")) * 10**23 #6.39*(10**23) = mass of Mars (kg)
r = float(input("What is the radius of Mars?\n____x 10^6> "))*10**6 #3.3895*(10**6) = radius of Mars (m)
G = float(input("What is the gravitational constant G?\n ____x 10^-11> "))*10**-11 #6.67408*(10**-11)= gravitational constant
F_thrust = 4*10**7 # kg*m/s^2 Reverse thrust of rocket ### Will Have to change constant
v_ex = -4*10**(3) # m/s velocity of ejecting fuel ### Will have to change constant
mass_fuel = 2*10**5


#creating Rocket with current position, velocity, and current fuel left
rocket = Rocket()
self.altitude = r_init
self.velocity = v0
self.mass_fuel = mass_fuel

# Equations
def accel_grav(r):
    """
    Returns: current acceleration due to gravity at a distance r from mars
    """
    g = (G * m_mars) / (r+m_mars)**2
    return g

# Time for Simulation
dt = 1 # day
tmax = 500 # days
timestep = int(tmax/dt)

# Array for data allocation
time = np.zeros(timestep) # duration of landing/docking
m = np.zeros(timestep) # mass of rocket
x = np.zeros(timestep) # distance from Mars
v = np.zeros(timestep) # velocity (in m/s) of rocket
a = np.zeros(timestep) # acceleration (in m/s^2) of rocket

m[0] = self.mass + self.mass_fuel
x[0] = self.altitude
v[0] = v0
a[0] = -accel_grav(r_init)

ifinal = -1
for i in range(1, timestep):
    dm = F_thrust/v_ex
    if m[i-1] >= self.mass_rocket:
        m[i] = m[i-1] + dm * dt
    else:
        m[i] = m[i-1]
        F_thrust = 0
    a[i] = a[i-1] - accel_grav(x[i-1]) + F_thrust / m[i-1]
    v[i] = v[i-1] + a[i-1] * dt
    x[i] = x[i-1] + v[i-1] * dt
    time[i] = time[i-1] + dt
    if x[i-1] <=0:
        ifinal = i
        break

visualize(x, v, a, timestep, dt-1)
