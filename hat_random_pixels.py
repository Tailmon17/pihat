#!/usr/bin/env python
# this script will display letters with random colors on the Pi HAT
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
# assign a random integer between 0 and 255 to a variable named r
r=random.randint(0,255)
print("the random number is"), r, ("this time")

sense.set_pixel(2, 2, (0, 0, 0,))

sense.clear()
