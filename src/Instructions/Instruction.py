'''
Class that contains a variable for Sensor Instuction and Motion Instruction
'''

class Instruction():
    def __init__(this, sensor_instruction, motion_instruction,condition):
        this.sensor_instruction = sensor_instruction
        this.condition = condition
        this.motion_instruction = motion_instruction
    def get_sensor_instruction(this):
        return this.sensor_instruction
    def get_motion_instruction(this):
        return this.motion_instruction
    def isCompleted(this):
        if(this.sensor_instruction.get_sensor_info().getData() == this.condition):
            return True
        else:
            return False