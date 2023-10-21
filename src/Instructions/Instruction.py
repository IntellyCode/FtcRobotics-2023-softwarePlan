'''
Class that contains a variable for Sensor Instuction and Motion Instruction
'''
from Instructions.Sensor import SensorInstruction
from Instructions.Motion import MotionInstruction
class Instruction():
    
    """
    For now the instruction takes as a parameter a condition (True or False)
    to know when its complete
    
    For more complicated sensors, we can have a Condition Object that can be passed in and will ensure 
    the instruction is complete when the condition is met
    """
    def __init__(this, sensor_instruction:SensorInstruction, motion_instruction:MotionInstruction,condition:bool):
        this.sensor_instruction = sensor_instruction
        this.condition = condition
        this.motion_instruction = motion_instruction
        
    """
    Getter function for each instruction
    The instruction object it self does not perform any data validation or execution.
    Its a wrapper, to bring together Sensor and Motion Instructions
    """
    def get_sensor_instruction(this):
        return this.sensor_instruction
    def get_motion_instruction(this):
        return this.motion_instruction
    
    """
    The completed function is used in the controller
    to check if the instruction is complete
    
    For now it simply checks if the sensor instruction met the condition
    
    In the future we can use the Condtion object to check if the instruction is complete
    """
    def isCompleted(this):
        if(this.sensor_instruction.get_sensor_info().getData() == this.condition):
            return True
        else:
            return False