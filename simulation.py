import pygame
import sys
from pathFind import *
import numpy as np
from AquaticDrones import *
np.random.seed(1)

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
thicc = 12

# Supervisor size constants
SUPERVISOR_POS = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

# Drone constants
num_drones = 9
DRONE_OFFSET = 40
DRONE_SPEED = 0.1

# Algae Processing


def makeAlgae(pattern, x, y, xmax, ymax):
    ALGAE_COVERAGE = 0.3

    if (np.linalg.norm(np.array(SUPERVISOR_POS) - np.array([x * thicc + thicc / 2, y * thicc + thicc / 2])) < 6 + DRONE_OFFSET):
        return False

    if pattern == "outer":
        strength = np.min([x, y, xmax - x, ymax - y])
        if (np.random.random() < 30 / (strength**2)):
            return True
        else:
            return False
    else:
        return ALGAE_COVERAGE


# Environment Setup
pygame.init()
screen = pygame.display.set_mode(SIZE)
background = pygame.image.load('lake_v2.png').convert()
screen.blit(background, (0, 0))

algae = pygame.image.load('algae.png')

screen.lock()
background_arr = pygame.surfarray.array3d(screen)
screen.unlock()

supervisor = pygame.image.load("supervisor.png")
AQSupervisor = AquaticSupervisor(-1, SUPERVISOR_POS, [], supervisor)
centerblit(screen, supervisor, SUPERVISOR_POS)
droneImage = "Drone.png"
drone = pygame.image.load(droneImage).convert()
angleFromCenter = (2 * np.pi) / num_drones

# Grid
SHOW_GRID = False

if SHOW_GRID:
    for row in range(thicc, WINDOW_HEIGHT, thicc):
        pygame.draw.line(screen, (0, 0, 0), (0, row), (WINDOW_WIDTH, row))

    for col in range(thicc, WINDOW_WIDTH, thicc):
        pygame.draw.line(screen, (0, 0, 0), (col, 0), (col, WINDOW_HEIGHT))

grid_rows = WINDOW_HEIGHT // thicc
grid_cols = WINDOW_WIDTH // thicc

grid = []

for row in range(grid_rows):
    curr_row = []

    for col in range(grid_cols):
        pixel = background_arr[col * thicc +
                               thicc // 2][row * thicc + thicc // 2]
        if (pixel[2] > 200):
            if (np.random.random() < makeAlgae("outer", col, row, grid_cols, grid_rows)):
                curr_row.append(Node((row, col), True, True))
            else:
                curr_row.append(Node((row, col), True, False))
        else:
            curr_row.append(Node((row, col), False, False))

    grid.append(curr_row)


for row in range(grid_rows):
    for col in range(grid_cols):
        if grid[row][col].isMustVisitNode:
            centerblit(screen, algae, (col * thicc +
                       thicc // 2, row * thicc + thicc // 2))

for i in range(num_drones):
    droneXPos = SUPERVISOR_POS[0] + DRONE_OFFSET * np.cos(i * angleFromCenter)
    droneYPos = SUPERVISOR_POS[1] + DRONE_OFFSET * np.sin(i * angleFromCenter)

    currentDrone = AquaticDrone(
        i, (droneXPos, droneYPos), (DRONE_SPEED, i * angleFromCenter), drone)
    centerblit(screen, drone, (droneXPos, droneYPos))
    AQSupervisor.addDrone(currentDrone)


# RRT Path Planning
STEP_SIZE = 0.1
max_depth = 7


def isValid(pixel, x, y):
    if np.linalg.norm(np.array([x, y]) - np.array(SUPERVISOR_POS)) < 33:
        return False

    if pixel[2] > 200: 
        return True

    else:
        return False


def samplePoint(map, paths):
    strength_threshold = 1000

    for i in range(5):
        xsamp = np.random.randint(0, WINDOW_WIDTH)
        ysamp = np.random.randint(0, WINDOW_HEIGHT)

        while not isValid(map[xsamp][ysamp], xsamp, ysamp):
            xsamp = np.random.randint(0, WINDOW_WIDTH)
            ysamp = np.random.randint(0, WINDOW_HEIGHT)

        strength = np.linalg.norm(
            np.array(SUPERVISOR_POS) - np.array([xsamp, ysamp]))

        if np.random.random() < (strength / strength_threshold)**2:
            return (xsamp, ysamp)

        strength_threshold = strength_threshold - 150

    return (xsamp, ysamp)


def generatePath(map, sampled, path, step):
    delta = np.array(sampled) - np.array(path[-1])
    dist = np.linalg.norm(delta)
    n = int(np.floor(dist / step))
    for i in range(n):
        x = path[-1][0] + delta[0] / dist * step
        y = path[-1][1] + delta[1] / dist * step

        if isValid(map[int (x)][int (y)], x, y):
            path.append((x, y))
        else:
            break


paths = []
for drone in AQSupervisor.dronesList:
    paths.append([drone.position])


for depth in range(max_depth):
    for i in range(num_drones):
        sampled = samplePoint(background_arr, paths[i])
        generatePath(background_arr, sampled, paths[i], STEP_SIZE)


depth = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for i in range(num_drones):
        moveDrone(screen, background,
                  AQSupervisor.dronesList[i], paths[i][depth])

    depth = depth + 1

    pygame.display.update()
