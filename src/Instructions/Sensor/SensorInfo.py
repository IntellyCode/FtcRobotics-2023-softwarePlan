'''
Sensor Information class

1. Stores the sensor to read from
2. Stores the sensor data
'''

class SensorInfo:
    data=None
    def __init__(this, sensor):
        this.sensor = sensor
    def getData(this):
        return this.data
    def setData(this, data):
        this.data = data