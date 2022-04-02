from graphics import *
from AquaticDrone import *

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

# Environment Setup
# give title and dimensions
win = GraphWin('ASCRSim', WINDOW_WIDTH, WINDOW_HEIGHT, autoflush=False)

img = Image(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "starter_lake75.png")
img.draw(win)

# Initialize and draw Supervisor
super_p1 = Point(SUPERVISOR_POS[0] - SUPERVISOR_WIDTH,
                 SUPERVISOR_POS[1] - SUPERVISOR_HEIGHT)
super_p2 = Point(SUPERVISOR_POS[0] + SUPERVISOR_WIDTH,
                 SUPERVISOR_POS[1] + SUPERVISOR_HEIGHT)
supervisor = Rectangle(super_p1, super_p2)

supervisor.draw(win)
supervisor.setFill("black")

# Init and draw drones
bots = []
for i in range(num_drones):
    bots.append(Circle(Point(400 + 20 * i, 400 + 20 * i), DRONE_RADIUS))
    bots[i].setFill("red")
    bots[i].draw(win)


# Move drones and update the window
for i in range(100):
    for j in range(num_drones):
        bots[j].move(2, 2)
        update(30)

# Exit
win.close()
