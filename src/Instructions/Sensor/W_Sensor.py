
"""
This class checks if the W key is presses or not in the read() method
"""
import keyboard
from Instructions.Sensor.Sensor import Sensor

"""

An extension of the Sensor class

"""

class W_Sensor(Sensor):
    def read():
        return keyboard.is_pressed('w')