# This program calculates the orbital velocity and period of a planet orbiting the sun at a given radius, 
# and then calculates the new orbital velocity and period for a planet that is 10 times farther from the sun.

# imports
import math #Import the math module to access mathematical functions and constants

# Variables
pi = math.pi
v = 0 #Orbital velocity in km/s
r = 1.496e8 #Orbital radius in km
P = 3.156e7 #Orbital period in seconds
G = 6.674e-11 #Gravitational constant in m^3 kg^-1 s^-2
M = 1.989e30 #Mass of the sun in kg

# Calculate orbital velocity
v = (2 * pi * r) / P
#print("The orbital velocity is:", v, "km/s") #Good
print("The orbital velocity is: {:5.2f} km/s".format(v)) #Better
r = 10*r #New orbital radius in km for a planet 10 times farther from the sun
# Calculate new orbital velocity
print("new orbital radius = {:.3e} km".format(r)) 
print("new orbital radius = {:.3f} km".format(r)) #mind the difference between e and f


# Calculate period in s from radius in km (Kepler's third law)
P = 2*pi*(G*M)**(-1/2)*(1e3*r)**(3/2) #Convert r from km to m for the calculation
# print period in years
print("new orbital period = {:.1f} yr".format(P/3.156e7)) #Convert P from seconds to years for the output

v = (2 * pi * r) / P
print("new orbital velocity = {:.2f} km/s".format(v))