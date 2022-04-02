import pygame
import sys
import numpy as np
from AquaticDrones import *


def centerblit(screen, image, pos):
    width, height = image.get_size()
    pos0 = pos[0] - np.round(width / 2)
    pos1 = pos[1] - np.round(height / 2)
    screen.blit(image, (pos0, pos1))


# Graphical constants
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 810
SIZE = WINDOW_WIDTH, WINDOW_HEIGHT

# Supervisor size constants
SUPERVISOR_POS = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

# Drone constants
num_drones = 3
DRONE_OFFSET = 40
DRONE_SPEED = 1

# Environment Setup
# give title and dimensions
pygame.init()
screen = pygame.display.set_mode(SIZE)
background = pygame.image.load('starter_lake75.png').convert()
screen.blit(background, (0, 0))


supervisor = pygame.image.load("supervisor.png")
AQSupervisor = AquaticSupervisor(-1, SUPERVISOR_POS, [], supervisor)
centerblit(screen, supervisor, SUPERVISOR_POS)
droneImage = "Drone.png"
drone = pygame.image.load(droneImage).convert()
angleFromCenter = (2 * np.pi) / num_drones

for i in range(num_drones):
    droneXPos = SUPERVISOR_POS[0] + DRONE_OFFSET * np.cos(i * angleFromCenter)
    droneYPos = SUPERVISOR_POS[1] + DRONE_OFFSET * np.sin(i * angleFromCenter)

    currentDrone = AquaticDrone(
        i, (droneXPos, droneYPos), (DRONE_SPEED, i * angleFromCenter), drone)
    centerblit(screen, drone, (droneXPos, droneYPos))
    AQSupervisor.addDrone(currentDrone)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


pygame.display.update()
