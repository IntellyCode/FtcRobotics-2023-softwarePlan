'''
SensorComponent class

1. Contains a variable that stores the current sensor instruction
2. Uses this sensor instruction to read data from appropriate sensors
3. Saves the sensor data to the sensor instruction
'''
from Instructions.Sensor.SensorInstruction import SensorInstruction

class SensorComponent():
    def set_sensor_instruction(this, sensor_instruction):
        this.sensor_instruction = sensor_instruction

    def get_sensor_instruction(this):
        return this.sensor_instruction
    
    def perform_sensor_instruction(this):
        sensorInfo = this.sensor_instruction.get_sensor_info()
        sensorInfo.setData(sensorInfo.sensor.read())