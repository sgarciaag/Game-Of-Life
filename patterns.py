"""
Use this code to represent all the possible patterns to check for
"""
import numpy as np

ON = 255
OFF = 0
vals = [ON, OFF]

blocks = np.array([
    [OFF, OFF, OFF, OFF],
    [OFF, ON, ON, OFF],
    [OFF, ON, ON, OFF],
    [OFF, OFF, OFF, OFF]
])

beehives = np.array([
    [OFF, ON, ON, OFF],
    [ON, OFF, OFF, ON],
    [OFF, ON, ON, OFF]
])

loafs = np.array([
    [OFF, ON, ON, OFF],
    [ON, OFF, OFF, ON],
    [OFF, ON, OFF, ON],
    [OFF, OFF, ON, OFF]
])

boats = np.array([
    [ON, ON, OFF],
    [ON, OFF, ON],
    [OFF, ON, OFF]
])

tubs = np.array([
    [OFF, ON, OFF],
    [ON, OFF, ON],
    [OFF, ON, OFF]
])

blinker1 = np.array([
    [OFF, ON, OFF],
    [OFF, ON, OFF],
    [OFF, ON, OFF]
])

blinker2 = np.array([
    [OFF, OFF, OFF],
    [ON, ON, ON],
    [OFF, OFF, OFF]
])

toad1 = np.array([
    [OFF, OFF, ON, OFF],
    [ON, OFF, OFF, ON],
    [ON, OFF, OFF, ON],
    [OFF, ON, OFF, OFF]
])

toad2 = np.array([
    [OFF, OFF, OFF, OFF],
    [OFF, ON, ON, ON],
    [ON, ON, ON, OFF],
    [OFF, OFF, OFF, OFF]
])

beacon1 = np.array([
    [ON, ON, OFF, OFF],
    [ON, ON, OFF, OFF],
    [OFF, OFF, ON, ON],
    [OFF, OFF, ON, ON]
])

beacon2 = np.array([
    [ON, ON, OFF, OFF],
    [ON, OFF, OFF, OFF],
    [OFF, OFF, OFF, ON],
    [OFF, OFF, ON, ON]
])

glider1 = np.array([
    [OFF, ON, OFF], 
    [OFF, OFF, ON], 
    [ON, ON, ON]
])

glider2 = np.array([
    [ON, OFF, ON], 
    [OFF, ON, ON], 
    [OFF, ON, OFF]
])

glider3 = np.array([
    [OFF, OFF, ON], 
    [ON, OFF, ON], 
    [OFF, ON, ON]
])

glider4 = np.array([
    [ON, OFF, OFF], 
    [OFF, ON, ON], 
    [ON, ON, OFF]
])

spaceship1 = np.array([
    [ON, OFF, OFF, ON, OFF],
    [OFF, OFF, OFF, OFF, ON],
    [ON, OFF, OFF, OFF, ON],
    [OFF, ON, ON, ON, ON]
])

spaceship2 = np.array([
    [OFF, OFF, ON, ON, OFF],
    [ON, ON, OFF, ON, ON],
    [ON, ON, ON, ON, OFF],
    [OFF, ON, ON, OFF, OFF]
])

spaceship3 = np.array([
    [OFF, OFF, ON, ON, OFF],
    [ON, ON, OFF, ON, ON],
    [ON, ON, ON, ON, OFF],
    [OFF, ON, ON, OFF, OFF]
])

spaceship4 = np.array([
    [OFF, ON, ON, ON, ON],
    [ON, OFF, OFF, OFF, ON],
    [OFF, OFF, OFF, OFF, ON],
    [ON, OFF, OFF, ON, OFF]
])

    