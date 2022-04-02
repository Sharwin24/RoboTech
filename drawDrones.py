from graphics import *
from AquaticDrones import *
import numpy as np

# Graphical constants
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 810

# Supervisor size constants
SUPERVISOR_POS = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
SUPERVISOR_WIDTH = 35
SUPERVISOR_HEIGHT = SUPERVISOR_WIDTH


# drone constants
num_drones = 5
DRONE_RADIUS = 7
DRONE_DISTANCE_FROM_SUPERVISOR = 14

# Environment Setup
# give title and dimensions
win = GraphWin('ASCRSim', WINDOW_WIDTH, WINDOW_HEIGHT, autoflush=False)
backgroundImage = Image(
    Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "starter_lake75.png")
backgroundImage.draw(win)

# Initialize and draw Supervisor
supervisorPoint1 = Point(SUPERVISOR_POS[0] - SUPERVISOR_WIDTH,
                         SUPERVISOR_POS[1] - SUPERVISOR_HEIGHT)
supervisorPoint2 = Point(SUPERVISOR_POS[0] + SUPERVISOR_WIDTH,
                         SUPERVISOR_POS[1] + SUPERVISOR_HEIGHT)
supervisorImage = Rectangle(supervisorPoint1, supervisorPoint2)
AQSupervisor = AquaticSupervisor(-1, SUPERVISOR_POS, [], supervisorImage)

AQSupervisor.image.draw(win)
AQSupervisor.image.setFill("black")

# Init and draw drones
bots = []
angleFromCenter = 360 / num_drones
for i in range(num_drones):
    droneImg = Circle(
        Point(SUPERVISOR_POS[0], SUPERVISOR_POS[1]), DRONE_RADIUS)
    currentDrone = AquaticDrone(i, (0, 0), (0, 90), AQSupervisor, droneImg)
    currentDrone.image.setFill("red")
    currentDrone.image.draw(win)
    AQSupervisor.addDrone(currentDrone)


# Move drones and update the window
for i in range(100):
    for j in range(num_drones):
        bots[j].move(2, 2)
        update(30)

# Exit
win.close()
