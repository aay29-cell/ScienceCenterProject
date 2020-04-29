from constants import *
import matplotlib.pyplot as plt
import numpy as np


class Rocket:


    def __init__(self):
        self.mass_rocket = MASS_ROCKET
        self.mass_fuel = MASS_FUEL
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
        nt = int(tmax / dt)
        s, v, a = np.zeros(nt), np.zeros(nt), np.zeros(nt)
        s[0] = 0.0
        v[0] = 0.0
        a[0] = 0.0

        launch_fuel = self.mass_fuel  # calculate what percent of total fuel used for launch

        for i in range(1, nt):
            force = self.force_thrust() - self.force_gravity(altitude=s[i-1]) - self.force_drag(altitude=s[i-1], velocity=v[i-1])
            print(i, self.force_thrust(), self.force_gravity(altitude=s[i-1]), self.force_drag(altitude=s[i-1], velocity=v[i-1]))
            self.consume_fuel()
            if self.mass_fuel < 0: 
                crashed = True
            a[i] = force / (self.mass_rocket + self.mass_fuel)
            v[i] = a[i-1] * dt + v[i-1]
            s[i] = 0.5 * a[i-1] * dt**2 + v[i-1] * dt + s[i-1]

        self.visualize(s, v, a, i, dt)


    def consume_fuel(self):
        """
        Consumes fuel for a single time step
        """
        self.mass_fuel -= 0.5

    def force_gravity(self, altitude):
        """
        Calculates the force of gravity currently acting on the rocket

        Parameters
        ----------
        altitude:
            the current height of the rocket
        """
        return GRAVITATIONAL_CONSTANT * (self.mass_rocket + self.mass_fuel) * MASS_EARTH / (RADIUS_EARTH + altitude)**2


    def force_drag(self, altitude, velocity):
        """
        Returns the force of drag curently acting on the rocket

        Parameters
        ----------
        altitude:
            the current altitude of the rocket
        velocity:
            the current velocity of the rocket in m/s
        """
        return 0.5 * DRAG_COEFF * ORTH_SURFACE_AREA * self.rho(altitude) * velocity**2


    def force_thrust(self):
        return BOOSTER_THRUST


    def wind(self, altitude):
        """
        Returns the force of wind acting on the rocket

        Parameters
        ----------
        altitude:
            the altitude to find wind velocity
        """
        wind_velocity = 0
        return 0.5 * self.rho(altitude) * wind_velocity**2 * ORTH_SURFACE_AREA


    def rho(self, altitude):
        """
        Calculates the current air density in kg/m^3

        Parameters
        ----------
        altitude:
            the altitude to find desired air density

        Source
        ------
        NASA:
            https://www.grc.nasa.gov/WWW/K-12/airplane/atmosmet.html
        """
        R = 287.05  # Specific gas constant for dry RADIUS_EARTH
        if altitude > 25000:
            T = -131.21 + 0.003 * altitude
            p = 2.488 * ((T + 273.1) / 216.6)**-11.388
        elif altitude < 11000:
            T = 15.04 - 0.00649 * altitude
            p = 101.29 * ((T + 273.1) / 288.08)**5.256
        else:
            T = -56.64
            p = 22.65 * np.exp(1.73 - 0.000157 * altitude)
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
        x = np.arange(0, int(len(s)*dt), dt)

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


rocket = Rocket()
rocket.launch(100, 0.1)
