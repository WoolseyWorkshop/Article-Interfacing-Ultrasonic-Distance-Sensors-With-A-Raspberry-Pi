#!/usr/bin/env python3

"""
hcsr04_array.py

Description:
Reads an array of HC-SR04, or compatible, ultrasonic distance sensors and
provides the ability to specify the sensor sampling rate.

Circuit:
- Four HC-SR04 sensors connected to
  S0 trigger: BCM pin 19, physical pin 35
     S0 echo: BCM pin 13, physical pin 33
  S1 trigger: BCM pin 27, physical pin 13
     S1 echo: BCM pin 17, physical pin 11
  S2 trigger: BCM pin 21, physical pin 40
     S2 echo: BCM pin 20, physical pin 38
  S3 trigger: BCM pin 24, physical pin 18
     S3 echo: BCM pin 23, physical pin 16

Libraries:
- time Standard Library (https://docs.python.org/3/library/time.html)
  - Access to time function.
- GPIO Zero (https://gpiozero.readthedocs.io)
  - Control GPIO and attached devices, including DistanceSensor class.

Notes:
- BEWARE: Make sure to use voltage dividers or level shifters when connecting
  5 V sensors to the Raspberry Pi in order to not destroy the GPIO bank.
- GPIO resources are automatically cleaned up by GPIO Zero library upon exit.

TODO:
- None.

Author(s):
- Created by John Woolsey on 04/27/2020.
- Modified by John Woolsey on 05/01/2020.

Copyright (c) 2020 Woolsey Workshop.  All rights reserved.
"""


# Libraries
from time import time
from gpiozero import DistanceSensor


# Global Constants
SAMPLE_RATE = 1.0  # sensor sampling rate in Hz


# Global Instances
dist_sensors = [  # using maximum rated distance for HC-SR04
    DistanceSensor(echo=13, trigger=19, max_distance=4),
    DistanceSensor(echo=17, trigger=27, max_distance=4),
    DistanceSensor(echo=20, trigger=21, max_distance=4),
    DistanceSensor(echo=23, trigger=24, max_distance=4)
]


# Functions

def show_dist_sensors():
    """Shows configuration of all distance sensors."""
    print("Distance sensors configured:")
    for index, sensor in enumerate(dist_sensors):
        print("%d: echo = %s, trigger = %s, max_distance = %.1f, threshold_distance = %.1f"
              % (index, sensor.echo, sensor.trigger, sensor.max_distance,
                 sensor.threshold_distance))
    print()

def read_dist_sensors():
    """Read all distance sensors."""
    for index, sensor in enumerate(dist_sensors):
        print("Distance sensor %d read %.1f cm."
              % (index, sensor.distance * 100))


# Main
show_dist_sensors()
previous_time = time()  # time in seconds
print("Press CTRL-C to exit.\n")
while True:
    current_time = time()  # time in seconds
    if current_time - previous_time >= 1.0/SAMPLE_RATE:
        read_dist_sensors()
        previous_time = current_time
