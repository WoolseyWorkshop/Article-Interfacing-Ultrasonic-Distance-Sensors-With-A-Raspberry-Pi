#!/usr/bin/env python3

"""
hcsr04_simple.py

Description:
Reads an HC-SR04, or compatible, ultrasonic distance sensor and prints distance
values to the screen.

Circuit:
- HC-SR04 sensor connected to
  trigger: BCM pin 24, physical pin 18
     echo: BCM pin 23, physical pin 16

Libraries:
- time Standard Library (https://docs.python.org/3/library/time.html)
  - Access to sleep function.
- GPIO Zero (https://gpiozero.readthedocs.io)
  - Control GPIO and attached devices, including DistanceSensor class.

Notes:
- BEWARE: Make sure to use voltage dividers or level shifters when connecting
  5 V sensors to the Raspberry Pi in order to not destroy the GPIO bank.
- GPIO resources are automatically cleaned up by GPIO Zero library upon exit.

TODO:
- None.

Author(s):
- Created by John Woolsey on 04/23/2020.
- Modified by John Woolsey on 05/01/2020.

Copyright (c) 2020 Woolsey Workshop.  All rights reserved.
"""


# Libraries
from time import sleep
from gpiozero import DistanceSensor


# Global Instances
dist_sensor = DistanceSensor(echo=23, trigger=24, max_distance=4)  # using maximum rated distance for HC-SR04


# Main
print("Press CTRL-C to exit.\n")
while True:
    print("Distance sensor read %.1f cm." % (dist_sensor.distance * 100))
    sleep(1)  # wait a second between readings
