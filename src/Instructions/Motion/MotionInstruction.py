
"""
This is the motion instruction class

Everything to do with motion as well as lifts and airplanes comes here

For now, the perform method just prints the motion instruction and motion Info

Also,
Motion Instruction will be either of type "Definite" or "Indefinite"

A "Definite" action is one where we know a precise measurmenet, e.g 10 meters forward

An "Indefinite" action is one where we do not know a precise measurement, 
e.g move forward until the sensor reads a certain value
"""
class MotionInstruction():
    def __init__(this, motionInfo):
        this.motionInfo = motionInfo
    def perform(this):
        print("Performing motion instruction:", this.motionInfo)