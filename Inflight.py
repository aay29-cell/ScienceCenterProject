"""
Science Center Project: Inflight Portion

Authors: Callen Reid, Ashley Fan, Cher Xu, Efrain Munoz
Date: 04/15/20
"""

import turtle
import launch
from constants import *
from turtle import *

SCALE = 75.0 / AU       # Scale 1 AU to 30 pixels

class planet(Turtle):
    """
    Class to represent a planet

    Attribute xloc: the x location of the planet
    Invariant: xloc is a float

    Attribute yloc: the y location of the planet
    Invariant: yloc is a float

    Attribute name: the name of the planet
    Invariant: name is a non-empty string
    """
    xloc = yloc = 0.0
    name=''

class spaceship(launch.Rocket,planet):
    """
        Class to represent a spaceship
        """

    # Attribute xloc: the x location of the spaceship
    # Invariant: xloc is a float >= 0.0 & <= 800.0
    #
    # Attribute yloc: the y location of the spaceship
    # Invariant: yloc is a float >= 0.0 & <= 800.0
    #
    # Attribute xVel: the magnitude of the x-component of velocity of the spaceship
    # Invariant: xVel is a float >= 0.0
    #
    # Attribute yVel: the magnitude of the y-component of velocity of the spaceship
    # Invariant: yVel is a float >= 0.0
    #
    # Attribute fuel: the remaining fuel in the spaceship
    # Invariant: fuel is a float >= 0.0

    def getX(self):
        """
        Returns the x location of the spaceship object
        """
        return self.xloc

    def setX(self, x):
        """
        Sets the x-location of the spaceship object

        Parameter x: The x-location of the spaceship object
        Precondition: x is a float >= 0.0 & <= 800.0
        """
        assert isinstance(x, float), 'Invalid type for x, x must be a float'
        assert (x >= 0.0 and x <= 800.0), 'Invalid value for x, x must be between 0 and 800 inclusive'
        self.xloc = x

    def getY(self):
        """
        Returns the y location of the spaceship object
        """
        return self.yloc

    def setY(self, y):
        """
        Sets the y location of the spaceship object

        Parameter y: The y-location of the spaceship object
        Precondition: y is a float >= 0.0 & <= 800.0
        """
        assert isinstance(y, float), 'Invalid type for y, y must be a float'
        assert (y >= 0.0 and y <= 800.0), 'Invalid value for y, y must be between 0 and 800 inclusive'
        self.yloc = y

    def getXVel(self):
        """
        Returns the x-velocity of the spaceship object
        """
        return self.vx

    def setXVel(self, vx):
        """
        Sets the x-velocity of the spaceship object

        Parameter vx: The x-velocity of the spaceship object
        Precondtion: vx is a float >=0.0
        """
        assert isinstance(vx, float), 'Invalid type for vx, vx must be a float'
        assert (vx >= 0.0), 'Invalid value for vx, vx must be greater than 0.0'

    def getYVel(self):
        """
        Returns the y-velocity of the spaceship object
        """
        return self.vy

    def setXVel(self, vy):
        """
        Sets the y-velocity of the spaceship object

        Parameter vy: The y-velocity of the spaceship object
        Precondtion: vy is a float >=0.0
        """

    def getFuel(self):
        """
        Returns the amount of remaining fuel in the spaceship object
        """
        return self.fuel

    def setFuel(self, f):
        """
        Sets the amount of fuel in the spaeship object

        Parameter f: The amount of fuel in the spaceship object
        Precondition: f is a float >=0.0
        """

    def __init__(self, alt, vel, angle, xCoord, yCoord):
        """
            Intiales a space spaceship

            Parameter alt: The initial altitude of the rocket
            Precondition: alt is a float > 0.0

            Parameter vel: The magnitude of the inital velocity of the rocket
            Precondition: vel is a float > 0.0

            Parameter ang: The angle of launch with respect to the positive x-axis
            Precondition: ang is a float in the range [0.0..360.0]
        """
        self.s = alt
        self.v = vel
        self.a = angle
        self.setX(xCoord + math.cos(angle)*alt)
        self.setY(yCord + math.sin(angle)*alt)
        planet.__init__(self)
        launch.Rocket.__init__(self)

    def thrust(self):
        self.vx=AU * -0.02 / 86400

def loop(system):
    timestep = 1*24*3600

    for body in system:
        body.goto(body.xloc*SCALE, body.yloc*SCALE)
        body.pendown()


def main():

    turtle.setup(800, 800)          # Set the window size to 800 by 800 pixels
    turtle.bgcolor("black")         # Set up the window with a black background

    sun = planet()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30
    sun.penup()
    sun.color('yellow')
    sun.shape('circle')
    sun.diameter = 1.3914 * 10**6
    sun.shapesize(2.0,2.0,1)

    mercury = planet()
    mercury.name = 'Mercury'
    mercury.mass = 3.302 * 10**23
    mercury.penup()
    mercury.color('gray')
    mercury.shape('circle')
    mercury.shapesize(0.2,0.2,1)
    mercury.diameter = 2440*2
    mercury.yloc = (1 * AU) *  -0.4608453269808703
    mercury.xloc = (1 * AU) *  -0.06333487572394930
    mercury.vy = AU * -0.002399853089908365  / 86400
    mercury.vx = AU * 0.02222816779156590 / 86400

    venus = planet()
    venus.name = 'Venus'
    venus.mass = 48.685 * 10**23
    venus.penup()
    venus.color('Khaki')
    venus.shape('circle')
    venus.shapesize(0.6,0.6,1)
    venus.diameter = 6051.893*2
    venus.yloc = (0.7262658 * AU) *  0.0525483
    venus.xloc = (0.7262658 * AU) *  0.7232002
    venus.vy = AU * 0.0200813  / 86400

    earth = planet()
    earth.name = 'Earth'
    earth.mass = MASS_EARTH
    earth.penup()
    earth.color('green')
    earth.shape('circle')
    earth.shapesize(0.6,0.6,1)
    earth.diameter = 12742
    earth.yloc = (1 * AU) *   0.96756
    earth.xloc = (1 * AU) *  -0.17522

    mars = planet()
    mars.name = 'Mars'
    mars.mass = MASS_MARS
    mars.penup()
    mars.color('red')
    mars.shape('circle')
    mars.shapesize(0.5,0.5,1)
    mars.diameter = 3389.92*2
    mars.yloc = (1 * AU) *  -0.857574644771996
    mars.xloc = (1 * AU) *  -1.320107604952232

    saturnV = spaceship(launch.rocket.s,launch.rocket.b,launch.rocket.a,earth.xloc,earth.yloc)
    saturnV.name = "Saturn V"
    saturnV.penup()
    saturnV.shape('classic')
    saturnV.color('black')
    saturnV.shapesize(0.3,0.3,1)

    loop([sun, mercury, venus, earth, mars, saturnV])


if __name__ == '__main__':          # The code starts here
    main()                          # Goes to the function called main (line 82)
