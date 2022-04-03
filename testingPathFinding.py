from pathFind import *
import numpy as np

GRID_SIZE = 8
grid = []
DRONE_POS = Position(2, 2)

for row in range(GRID_SIZE):
    gridRow = []
    for col in range(GRID_SIZE):
        canGo = row != 0 and row != GRID_SIZE - 1 and col != 0 and col != GRID_SIZE - 1
        isDrone = row == 2 and col == 2
        gridRow.append(
            Node(Position(col, row), canGo and not isDrone, np.random.random() <= 0.1 and canGo and not isDrone))
    grid.append(gridRow)

navGrid = NavigationGrid(grid)

MVNodes = []
for r in range(GRID_SIZE):
    for c in range(GRID_SIZE):
        n = grid[r][c]
        assert(isinstance(n, Node))
        if n.position == DRONE_POS:
            print("x", end="")
        elif n.isMustVisitNode:
            print("@", end="")
            MVNodes.append(n.position)
        elif n.isTraversable:
            print(".", end="")
        else:
            print("#", end="")
    print("\n")
startState = StateSpace(DRONE_POS, [], MVNodes, navGrid)
print("# of MVNodes: " + str(len(MVNodes)))
distance_path = shortestPath(startState)
print(str(distance_path[0]) + " | " + str(distance_path[1]))
