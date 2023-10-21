'''
MotionComponent class

1. Contains a variable that stores the current motion instruction
2. Uses this motion instruction to read data from appropriate motions
3. Saves the motion data to the motion instruction
'''
from Instructions.Motion.MotionInstruction import MotionInstruction

class MotionComponent():
    def set_motion_instruction(this, motion_instruction):
        this.motion_instruction = motion_instruction

    def get_motion_instruction(this):
        return this.motion_instruction
    
    def perform_motion_instruction(this):
        this.motion_instruction.perform()