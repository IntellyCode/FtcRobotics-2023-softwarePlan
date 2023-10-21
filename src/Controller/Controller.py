'''
Controller class:
1. Contains the array of instructions
2. Loops through the instructions and forwards execution to appropriate components
'''
import os
from Components.SensorComponent import SensorComponent
from Components.MotionComponent import MotionComponent

from Instructions import Instruction as I

from Instructions.Sensor import SensorInstruction as SIns, SensorInfo as SI, A_Sensor as AS, W_Sensor as WS
from Instructions.Motion import MotionInstruction as MI

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Controller():
    instructions = [I.Instruction(SIns.SensorInstruction(SI.SensorInfo(WS.W_Sensor)), MI.MotionInstruction("W instruction"),True),
                    I.Instruction(SIns.SensorInstruction(SI.SensorInfo(AS.A_Sensor())), MI.MotionInstruction("A instruction"),True)]
    current_instruction = None
    completed = False
    
    def __init__(this):
        this.SensorComponent = SensorComponent()
        this.MotionComponent = MotionComponent()
        this.current_instruction = this.instructions[0]
        this.SensorComponent.set_sensor_instruction(this.current_instruction.get_sensor_instruction())
        this.MotionComponent.set_motion_instruction(this.current_instruction.get_motion_instruction())
        
        
    def loop(this):
        clear_console()

        if(this.current_instruction.isCompleted()):
            if(this.instructions.index(this.current_instruction) == len(this.instructions)-1):
                this.completed = True
                return
            this.current_instruction = this.instructions[this.instructions.index(this.current_instruction)+1]
            this.SensorComponent.set_sensor_instruction(this.current_instruction.get_sensor_instruction())
            this.MotionComponent.set_motion_instruction(this.current_instruction.get_motion_instruction())
        this.SensorComponent.perform_sensor_instruction()
        print("Current action sensor data",this.current_instruction.get_sensor_instruction().get_sensor_info().getData())
        this.MotionComponent.perform_motion_instruction()

