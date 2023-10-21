'''
SensorComponent class

1. Contains a variable that stores the current sensor instruction
2. Uses this sensor instruction to read data from appropriate sensors
3. Saves the sensor data to the sensor instruction
'''

#Import the necessary type for hinting
from Instructions.Sensor.SensorInstruction import SensorInstruction

class SensorComponent():
    #This method is called when a new instruction is about to be executed
    def set_sensor_instruction(this, sensor_instruction: SensorInstruction):
        this.sensor_instruction = sensor_instruction
    
    """
    This method is called when the sensor instruction is to be executed
    1. It gets the sensor info from the sensor instruction
    2. It reads the data from the sensor
    3. It saves the data to the sensor info
    
    In this example, we have a simplified version of the code.
    
    In the Java example a loop is used to read data from multiple sensors in a single instruction.
    """
    def perform_sensor_instruction(this):
        sensorInfo = this.sensor_instruction.get_sensor_info()
        sensorInfo.setData(sensorInfo.sensor.read())