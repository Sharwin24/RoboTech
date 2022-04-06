from pathFind import *
import numpy as np

GRID_SIZE = 8  # Above 10 starts getting hard on complexity
MVNODE_RATE = 0.05  # 0.1 for more MV Nodes
DRONE_POS = Position(int(np.random.random() * GRID_SIZE - 1),
                     int(np.random.random() * GRID_SIZE - 1))

grid = []
for row in range(GRID_SIZE):
    gridRow = []
    for col in range(GRID_SIZE):
        canGo = row != 0 and row != GRID_SIZE - 1 and col != 0 and col != GRID_SIZE - 1
        isDrone = row == DRONE_POS.x and col == DRONE_POS.y
        gridRow.append(
            Node(Position(col, row), canGo and not isDrone, np.random.random() <= MVNODE_RATE and canGo and not isDrone))
    grid.append(gridRow)

navGrid = NavigationGrid(grid)

MVNodes = set()
for r in range(GRID_SIZE):
    for c in range(GRID_SIZE):
        n = grid[r][c]
        assert(isinstance(n, Node))
        if n.position == DRONE_POS:
            print(" DR ", end="")
        elif n.isMustVisitNode:
            print(" MV ", end="")
            MVNodes.add(n.position)
        elif n.isTraversable:
            print(" TV ", end="")
        else:
            print(" NT ", end="")
    print("\n")
startState = StateSpace(DRONE_POS, [DRONE_POS], MVNodes, navGrid)
print("# of MustVisitNodes: " + str(len(MVNodes)))
distance_path = shortestPath(startState)
print("Nodes Traversed: " +
      str(len(distance_path)) + " | Path: " + str(distance_path))
print("Drone Pos: " + str(DRONE_POS))
