'''
Controller class:
1. Contains the array of instructions
2. Loops through the instructions and forwards execution to appropriate components
'''
import os

#Importing the copmpnents
from Components.SensorComponent import SensorComponent
from Components.MotionComponent import MotionComponent

#Importing the instructions
from Instructions import Instruction as I
from Instructions.Sensor import SensorInstruction as SIns, SensorInfo as SI, A_Sensor as AS, W_Sensor as WS
from Instructions.Motion import MotionInstruction as MI


#Helper function
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Controller():
    
    """
    This is the list of instructions.
    For now it is a static variable
    But in the future we can have a SequenceDesigner class that can design a sequence of instructions
    Based on dynamic inputs from the user/sensors
    """
    instructions = [I.Instruction(SIns.SensorInstruction(SI.SensorInfo(WS.W_Sensor)), MI.MotionInstruction("W instruction"),True),
                    I.Instruction(SIns.SensorInstruction(SI.SensorInfo(AS.A_Sensor())), MI.MotionInstruction("A instruction"),True)]
    """
    Variable storing the current instruction that is executed
    """
    current_instruction = None
    
    """
    Variable storing the completion status of the controller
    """
    completed = False
    
    
    """
    During initialisation:
    1. Initialise the SensorComponent
    2. Initialise the MotionComponent
    3. Set the current instruction to the first instruction in the list
    4. Set the sensor instruction of the SensorComponent to the sensor instruction of the current instruction
    5. Set the motion instruction of the MotionComponent to the motion instruction of the current instruction
    """
    def __init__(this):
        this.SensorComponent = SensorComponent()
        this.MotionComponent = MotionComponent()
        this.current_instruction = this.instructions[0]
        this.SensorComponent.set_sensor_instruction(this.current_instruction.get_sensor_instruction())
        this.MotionComponent.set_motion_instruction(this.current_instruction.get_motion_instruction())
        
        
    """
    This method is the loop that is run in the OpMode file
    """
    def loop(this):
        clear_console()

        """
        First we check if the insturction is completed
        """
        if(this.current_instruction.isCompleted()):
            """
            Secondly, we check if the instruction is the last instruction
            """
            if(this.instructions.index(this.current_instruction) == len(this.instructions)-1):
                this.completed = True
                return
            """
            If not, we will move onto the next instruction
            And split the instruction to its individual parts for execution
            """
            this.current_instruction = this.instructions[this.instructions.index(this.current_instruction)+1]
            this.SensorComponent.set_sensor_instruction(this.current_instruction.get_sensor_instruction())
            this.MotionComponent.set_motion_instruction(this.current_instruction.get_motion_instruction())
        """
        Here we exeucte the action. We first check the sensor data
        Then we perform the motion instruction.
        
        In the following example the motion instruction is indefinite,
        meaning that it runs until the sensor data is satisfied, which is checked in the Instruction class
        """
        this.SensorComponent.perform_sensor_instruction()
        print("Current action sensor data",this.current_instruction.get_sensor_instruction().get_sensor_info().getData())
        this.MotionComponent.perform_motion_instruction()

