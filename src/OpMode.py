from Controller.Controller import Controller
import time
# Path: src/Controller/Controller.py

controller = Controller()

while not controller.completed:
    controller.loop()
    # add a wait of 0.2 seconds to make the loop run slower
    time.sleep(0.2)
    
print("Completed all instructions")