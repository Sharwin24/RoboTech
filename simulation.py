import pygame, sys
import numpy as np
from AquaticDrones import *

# Functions
def centerblit(screen, image, pos):
    width, height = image.get_size()
    pos0 = pos[0] - np.round(width / 2)
    pos1 = pos[1] - np.round(height / 2)
    screen.blit(image, (pos0, pos1))

def moveDrone(screen, background, drone, newPos):
    oldPos = drone.position
    width, height = drone.image.get_size()
    oldx = oldPos[0] - np.round(width / 2)
    oldy = oldPos[1] - np.round(height / 2)
    pos = (oldx, oldy)
    
    screen.blit(background, pos, area=drone.image.get_rect(center=newPos))
    centerblit(screen, drone.image, newPos)

    drone.position = newPos



# Graphical constants
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 810
SIZE = WINDOW_WIDTH, WINDOW_HEIGHT

# Supervisor size constants
SUPERVISOR_POS = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

# Drone constants
num_drones = 4
DRONE_OFFSET = 40
DRONE_SPEED = 0.1

# Environment Setup
# give title and dimensions
pygame.init()
screen = pygame.display.set_mode(SIZE)
background = pygame.image.load('lake_v2.png').convert()
screen.blit(background, (0, 0))

screen.lock()
background_arr = pygame.surfarray.array2d(screen)
print(background_arr[0])

screen.unlock()


supervisor = pygame.image.load("supervisor.png")
AQSupervisor = AquaticSupervisor(-1, SUPERVISOR_POS, [], supervisor)
centerblit(screen, supervisor, SUPERVISOR_POS)
droneImage = "Drone.png"
drone = pygame.image.load(droneImage).convert()
angleFromCenter = (2 * np.pi) / num_drones

#Grid
thicc = 12

for row in range(thicc, WINDOW_HEIGHT, thicc):
    pygame.draw.line(screen, (0, 0, 0), (0, row), (WINDOW_WIDTH, row))

for col in range(thicc, WINDOW_WIDTH, thicc):
    pygame.draw.line(screen, (0, 0, 0), (col, 0), (col, WINDOW_HEIGHT))





for i in range(num_drones):
    droneXPos = SUPERVISOR_POS[0] + DRONE_OFFSET * np.cos(i * angleFromCenter)
    droneYPos = SUPERVISOR_POS[1] + DRONE_OFFSET * np.sin(i * angleFromCenter)

    currentDrone = AquaticDrone(i, (droneXPos, droneYPos), (DRONE_SPEED, i * angleFromCenter), drone)
    centerblit(screen, drone, (droneXPos, droneYPos))
    AQSupervisor.addDrone(currentDrone)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for curr_drone in AQSupervisor.dronesList:
        speed = curr_drone.vector[0]
        oldx, oldy = curr_drone.position
        newx = oldx + speed * np.cos(curr_drone.vector[1])
        newy = oldy + speed * np.sin(curr_drone.vector[1])

        newPos = (newx, newy)
        #moveDrone(screen, background, curr_drone, newPos)

    pygame.display.update()