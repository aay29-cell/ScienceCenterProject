"""
Science Center Project: Inflight Portion

Authors: Callen Reid, Ashley Fan, Cher Xu, Efrain Munoz
Date: 04/15/20
"""

import turtle
import constants
from tkinter import *
from math import *



SCALE = 75.0 / constants.AU       # Scale 1 AU to 30 pixels

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

    # def attraction(self, other, date):
    #
    #     # Compute x, y, and total distances between planet and other body
    #     rx = other.xloc-self.xloc
    #     ry = other.yloc-self.yloc
    #     r =  sqrt(rx**2+ry**2)
    #
    #     # Compute the overall force
    #     f = G*self.mass*other.mass/r**2
    #
    #     # Compute the angle between the hypotenuse and the adjacent side
    #     theta = atan2(ry,rx)
    #     # Compute the x component of the force
    #     fx = f*cos(theta)
    #     # Compute the y component of the force
    #     fy = f*sin(theta)
    #     # Return the x and y components of the force to the main loop
    #     return fx, fy


class spaceship(planet):
    """
    Class to represent a spaceship

    Attribute vx: x component of velocity of the spaceship
    Invariant: vx is a float

    Attribute vy: y component of velocity of the spaceship
    Invariant: vy is a float

    Attribute xloc: the x location of the spaceship
    Invariant: xloc is a float

    Attribute yloc: the y location of the spaceship
    Invariant: yloc is a float
    """
    def getX(self):
        """
        Returns the x location of the rocket
        """

    def setX(self,x):
        """
        Sets the ship object 
        """

    def getY(self):
        """
        Returns the y location of the rocket
        """

    def setY(self,y):
        """
        """

    def getXVel(self):
        """
        """
    def setXVel(self,v):
        """
        """
    def getAng(self):
        """
        """
    def setAng(self,a):
        """
        """

    def __init__(self,alt,vel,ang):
        """
        Intiales a space spaceship

        Parameter alt: The initial altitude of the rocket
        Precondition: alt is a float > 0.0

        Parameter vel: The magnitude of the inital velocity of the rocket
        Precondition: vel is a float > 0.0

        Parameter ang: The angle of launch with respect to the a straingt line
        path from Earth to Mars
        Precondition: ang is a float in the range [0.0..360.0]
        """

    def thrust(self):
        self.vx=AU * -0.02 / 86400

def loop(system):
#     timestep=??
    while(True):
        for body in system:
            body.goto(body.xloc*SCALE, body.yloc*SCALE)

#     while # Loop used to determine when the spaceship reaches mars (detmerine method to stop if it misses)

#
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
    earth.mass = 5.97 * 10**24
    earth.penup()
    earth.color('green')
    earth.shape('circle')
    earth.shapesize(0.6,0.6,1)
    earth.diameter = 12742
    earth.yloc = (1 * AU) *   0.96756
    earth.xloc = (1 * AU) *  -0.17522

    mars = planet()
    mars.name = 'Mars'
    mars.mass = 6.4171 * 10**23
    mars.penup()
    mars.color('red')
    mars.shape('circle')
    mars.shapesize(0.5,0.5,1)
    mars.diameter = 3389.92*2
    mars.yloc = (1 * AU) *  -0.857574644771996
    mars.xloc = (1 * AU) *  -1.320107604952232
#
#     saturnV = spaceship()
#     saturnV.name = 'Saturn V'
#     saturnV.mass = 48600 #From launch team
#     saturnV.penup()
#     saturnV.color('grey')
#     saturnV.shape('classic')
#     saturnV.shapesize(0.3,0.3,1)
#     saturnV.diameter = 10 #From launch team
#     saturnV.yloc = (1 * AU) *   0.97
#     saturnV.xloc = (1 * AU) *  -0.18
#     saturnV.vy = AU * -0.0031302  / 86400 #From launch team
#     saturnV.vx = AU * -0.017201 / 86400 #From launch team
    loop([sun,mercury,venus,earth,mars])

if __name__ == '__main__':          # The code starts here
    main()                          # Goes to the function called main (line 82)
