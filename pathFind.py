from dataclasses import dataclass
from turtle import position, width
from typing import List
from typing import Tuple
from typing import Set
from typing_extensions import Self
from utility import *
from queue import PriorityQueue


@dataclass
class Node():
    position: Position
    isTraversable: bool
    isMustVisitNode: bool

    def visitNode(self):
        self.isMustVisitNode = False

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Node):
            return self.position == __o.position and self.isMustVisitNode == __o.isMustVisitNode and self.isTraversable == __o.isTraversable
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.position) + hash(self.isMustVisitNode) + hash(self.isTraversable)

    def __repr__(self) -> str:
        return self.position.__repr__() + " | " + str(self.isMustVisitNode)


@dataclass
class NavigationGrid():
    grid: List[List[Node]]

    def inBounds(self, p: Position) -> bool:
        height = len(self.grid)
        width = len(self.grid[0])  # Assuming a 2D Matrix
        return p.x >= 0 and p.x < width and p.y >= 0 and p.y < height

    def isWall(self, p: Position) -> bool:
        return not self.grid[p.y][p.x].isTraversable


def getNeighbors(p: Position, navGrid: NavigationGrid) -> List[Position]:
    assert(isinstance(p, Position))
    up = Position(p.x, p.y + 1)
    down = Position(p.x, p.y - 1)
    left = Position(p.x - 1, p.y)
    right = Position(p.x + 1, p.y)
    upRight = Position(p.x + 1, p.y + 1)
    upLeft = Position(p.x - 1, p.y + 1)
    downRight = Position(p.x + 1, p.y - 1)
    downLeft = Position(p.x - 1, p.y - 1)
    possiblePositions = [up, down, left, right,
                         upRight, upLeft, downRight, downLeft]
    neighbors = []
    for p in possiblePositions:
        if navGrid.inBounds(p) and not navGrid.isWall(p):
            neighbors.append(p)
    return neighbors


@dataclass
class StateSpace():
    dronePosition: Position
    path: List[Position]
    mustVisitNodes: Set[Node]
    navigationGrid: NavigationGrid  # 2D Array of Position

    def getFCost(self) -> float:
        return self.getGCost() + self.getHCost()

    def getHCost(self) -> float:
        return 0  # No Heuristic yet

    def getGCost(self) -> float:
        return len(self.path)

    def isGoalState(self) -> bool:
        return len(self.mustVisitNodes) == 0

    def getSuccessors(self) -> List[Self]:
        neighborStates = getNeighbors(self.dronePosition, self.navigationGrid)
        successiveStates = []
        for p in neighborStates:
            newMVNodes = self.mustVisitNodes.copy()
            # Attempt to remove the MVNode if it exists
            for n in self.mustVisitNodes:
                if n.position == p:
                    newMVNodes.remove(n)
                # Add explored state to path to that state
                newPath = self.path.copy().append(p)
                newState = StateSpace(
                    p, newPath, newMVNodes, self.navigationGrid)
                successiveStates.append(newState)

        return successiveStates

    def getPath(self) -> List[Position]:
        return self.path

    def getMVNodes(self) -> Set[Position]:
        return self.mustVisitNodes

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, StateSpace):
            return self.mustVisitNodes == __o.mustVisitNodes and self.dronePosition == __o.dronePosition
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.dronePosition) + hash(self.mustVisitNodes)


def shortestPath(startingState: StateSpace) -> Tuple[int, List[Position]]:
    '''Finds the shortest path, such that all MVNodes are visited, from a starting state using A* search'''
    totalNodesTraversed = 0
    q = PriorityQueue()
    q.put((startingState.getFCost(), startingState))
    visitedStates = set()
    while q.not_empty:
        currentState = q.get()
        assert(isinstance(currentState[1], StateSpace))
        totalNodesTraversed += 1
        if currentState[1].isGoalState():
            return (totalNodesTraversed, currentState[1].getPath())
        neighbors = currentState[1].getSuccessors()
        for state in neighbors:
            if state not in q and state not in visitedStates:
                q.put(state)
        visitedStates.add(currentState[1])
    return None
