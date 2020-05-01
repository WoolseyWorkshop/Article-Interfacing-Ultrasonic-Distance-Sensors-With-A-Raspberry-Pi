#!/usr/bin/env python3

"""
hcsr04_range.py

Description:
Reads an HC-SR04, or compatible, ultrasonic distance sensor and determines
whether an object is within or outside of a particular range.

Circuit:
- HC-SR04 sensor connected to
  trigger: BCM pin 24, physical pin 18
     echo: BCM pin 23, physical pin 16

Libraries:
- signal Standard Library (https://docs.python.org/3/library/signal.html)
  - Access to pause function.
- GPIO Zero (https://gpiozero.readthedocs.io)
  - Control GPIO and attached devices, including DistanceSensor class.

Notes:
- BEWARE: Make sure to use voltage dividers or level shifters when connecting
  5 V sensors to the Raspberry Pi in order to not destroy the GPIO bank.
- GPIO resources are automatically cleaned up by GPIO Zero library upon exit.

TODO:
- None.

Author(s):
- Created by John Woolsey on 04/29/2020.
- Modified by John Woolsey on 05/01/2020.

Copyright (c) 2020 Woolsey Workshop.  All rights reserved.
"""


# Libraries
from signal import pause
from gpiozero import DistanceSensor


# Global Instances
dist_sensor = DistanceSensor(echo=23, trigger=24,
                             max_distance=4,  # maximum rated distance for HC-SR04
                             threshold_distance=0.3)  # trigger distance for range events


# Functions

def object_in_range(sensor):
    """Executed when the distance sensor detects an object in range."""
    print("Object detected in range (%.1f cm)." % (sensor.distance * 100))

def object_out_of_range(sensor):
    """Executed when the distance sensor detects an object out of range."""
    print("Object detected out of range (%.1f cm)." % (sensor.distance * 100))


# Main
print("Press CTRL-C to exit.\n")
dist_sensor.when_in_range = object_in_range
dist_sensor.when_out_of_range = object_out_of_range
pause()  # sleep until a process signal is received
