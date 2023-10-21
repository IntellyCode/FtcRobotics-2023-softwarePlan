
class MotionInstruction():
    completed=False
    def __init__(this, motionInfo):
        this.motionInfo = motionInfo
    def perform(this):
        print("Performing motion instruction:", this.motionInfo)
    def completed(this):
        pass