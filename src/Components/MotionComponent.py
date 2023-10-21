'''
MotionComponent class

1. Contains a variable that stores the current motion instruction
2. Uses this motion instruction to read data from appropriate motions
3. Saves the motion data to the motion instruction
'''
from Instructions.Motion.MotionInstruction import MotionInstruction

class MotionComponent():
    
    #This method is called when a new instruction is about to set
    def set_motion_instruction(this, motion_instruction:MotionInstruction):
        this.motion_instruction = motion_instruction
        
    #This method is called when the motion instruction is to be executed
    def perform_motion_instruction(this):
        this.motion_instruction.perform()