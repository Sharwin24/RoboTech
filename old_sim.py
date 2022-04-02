from graphics import *
import numpy as np
from AquaticDrones import *

# Graphical constants
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 810

# Supervisor size constants
SUPERVISOR_POS = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

# Drone constants
num_drones = 3
DRONE_OFFSET = 40
DRONE_SPEED = 1

# Environment Setup
# give title and dimensions
win = GraphWin('ASMRSim', WINDOW_WIDTH, WINDOW_HEIGHT, autoflush=False)
backgroundImage = Image(
    Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "starter_lake75.png")
backgroundImage.draw(win)

# Initialize and draw Supervisor
supervisorImage = "supervisor.png"
AQSupervisor = AquaticSupervisor(-1, SUPERVISOR_POS, [], Image(Point(SUPERVISOR_POS[0], SUPERVISOR_POS[1]), supervisorImage))

AQSupervisor.image.draw(win)

# Init and draw drones
droneImage = "Drone.png"
angleFromCenter = (2 * np.pi) / num_drones
for i in range(num_drones):
    droneXPos = SUPERVISOR_POS[0] + DRONE_OFFSET * np.cos(i * angleFromCenter)
    droneYPos = SUPERVISOR_POS[1] + DRONE_OFFSET * np.sin(i * angleFromCenter)
    droneImg = Image(Point(droneXPos, droneYPos), droneImage)

    currentDrone = AquaticDrone(i, (droneXPos, droneYPos), (DRONE_SPEED, i * angleFromCenter), droneImg)
    currentDrone.image.draw(win)
    AQSupervisor.addDrone(currentDrone)


# Move drones and update the window
for i in range(100):
    for drone in AQSupervisor.dronesList:
        drone.image.move(1, 1)
        update(30)

# Exit
win.close()