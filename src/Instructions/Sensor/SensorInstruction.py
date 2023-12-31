'''
SensorInstruction.py contains the SensorInstruction class, which is a subclass of the Instruction class.

1. Contains the sensor to read from
2. Contains the sensor data

'''
from Instructions.Sensor.SensorInfo import SensorInfo

class SensorInstruction:
    def __init__(this, sensorInfo: SensorInfo):
        this.sensorInfo = sensorInfo
    def get_sensor_info(this):
        return this.sensorInfo