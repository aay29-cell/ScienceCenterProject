from constants import *
import matplotlib.pyplot as plt
import numpy as np


class Rocket:


    def __init__(self, mass, fuel):
        self.mass = mass
        self.fuel = fuel
        self.altitude = 0.0
        self.velocity = 0.0
        self.acceleration = 0.0


    def launch(self, tmax, dt):
        """
        Launches the rocket and outputs graph of simulated trajectory

        Parameters
        ----------
        tmax : int
            the maximum number of time steps the run the simulation for
        dt : int
            the time between each time step
        """

        s = [self.altitude]
        v = [self.velocity]
        a = [self.acceleration]

        launch_fuel = self.fuel  # calculate what percent of total fuel used for launch

        for nt in np.arange(dt, tmax, dt):
            force = self.thrust() + self.wind() - self.gravity_force() - self.drag()
            if self.fuel > 0: self.consume_fuel()
            a.append(force / (self.mass + self.fuel))
            v.append(a[-1]*dt + v[-1])
            s.append(0.5*a[-1]*dt**2 + v[-1]*dt + s[-1])

        self.visualize(s, v, a, nt, dt)


    def consume_fuel(self):
        """
        Consumes fuel for a single time step
        """
        self.fuel -= 0.5

    def gravity_force(self):
        """
        Calculates the force of gravity currently acting on the rocket
        """
        return GRAVITATIONAL_CONSTANT * (self.mass + self.fuel) * MASS_EARTH / (RADIUS_EARTH + self.altitude)**2


    def drag(self):
        """
        Returns the force of drag curently acting on the rocket

        Parameters
        ----------
        rho : float
            density of fluid rocket travelling through
        """
        # TODO: model rho with equation based on current altitude
        return 0.5 * DRAG_COEFF * ORTH_SURFACE_AREA * self.rho() * self.velocity**2


    def thrust(self):
        return 1


    def wind(self):
        """
        Returns the force of wind acting on the rocket
        """
        wind_velocity = 0
        return 0.5 * self.rho() * wind_velocity**2 * ORTH_SURFACE_AREA


    def rho(self):
        """
        Calculates the current air density in kg/m^3

        Source: https://www.grc.nasa.gov/WWW/K-12/airplane/atmosmet.html
        """
        R = 287.05  # Specific gas constant for dry RADIUS_EARTH
        if self.altitude > 25000:
            T = -131.21 + 0.003 * self.altitude
            p = 2.488 * ((T + 273.1) / 216.6)**-11.388
        elif self.altitude < 11000:
            T = 15.04 - 0.00649 * self.altitude
            p = 101.29 * ((T + 273.1) / 288.08)**5.256
        else:
            T = -56.64
            p = 22.65 * np.exp(1.73 - 0.000157*self.altitude)
        return p / (0.2869 * (T + 273.1))


    def visualize(self, s, v, a, nt, dt):
        """
        Parameters
        ----------
        s : list
            the position of the rocket
        v : list
            the velocity of the rocket
        a : list
            the acceleration of the rocket
        nt : int
            the number of time steps
        dt : int
            the time between each time step
        """
        f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(8,8))
        f.tight_layout(pad=3.0)
        x = np.arange(0,nt+dt,dt)

        ax1.plot(x, s, 'b')
        ax1.set_ylabel('Altitude')
        ax1.set_title('Position vs. Time of Rocket Launch')

        ax2.plot(x, v, 'g')
        ax2.set_ylabel('Velocity')
        ax2.set_title('Velocity vs. Time of Rocket Launch')

        ax3.plot(x, a, 'r')
        ax3.set_ylabel('Acceleration')
        ax3.set_xlabel('Time (sec.)')
        ax3.set_title('Acceleration vs. Time of Rocket Launch')

        plt.show()


rocket = Rocket(10,1,1,1)
rocket.launch(100, 0.1)
