from graphics import *

# Global Vars
width = 1440
height = 810
num_drones = 5
supervisor_start = (720, 405)

# Environment Setup
win = GraphWin('ASCRSim', width, height, autoflush=False)  # give title and dimensions

img = Image(Point(width / 2, height / 2), "starter_lake75.png")
img.draw(win)

# Initialize Objects
bots = []
super_p1 = Point(supervisor_start[0] - 7, supervisor_start[1] - 7)
super_p2 = Point(supervisor_start[0] + 7, supervisor_start[1] + 7)
supervisor = Rectangle(super_p1, super_p2)

supervisor.draw(win)
supervisor.setFill("black")

theta = 0

for i in range(num_drones):
    bots.append(Circle(Point(400 + 20 * i, 400 + 20 * i), 5))
    bots[i].setFill("black")
    bots[i].draw(win)

# Movement Handling
for i in range(100):
    for i in range(5):
        bots[i].move(2, 2)

    update(30)

win.close()