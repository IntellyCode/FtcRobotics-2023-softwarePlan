'''
Sensor Information class

1. Stores the sensor to read from
2. Stores the sensor data
'''
from Instructions.Sensor.Sensor import Sensor
class SensorInfo:
    data=None
    
    """
    
    Any sensor can be passed in as a parameter
    
    """
    def __init__(this, sensor:Sensor):
        this.sensor = sensor
        
    """
    Getter and setter function for the data variable.
    
    Python does not have private variables, so we can access the data variable directly.
    """
    def getData(this):
        return this.data
    def setData(this, data):
        this.data = data