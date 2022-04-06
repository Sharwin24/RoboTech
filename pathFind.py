from dataclasses import dataclass
from typing import List
from typing import Tuple
from typing import Set
from typing_extensions import Self

from numpy import inf
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

    def isTraversable(self, p: Position) -> bool:
        return self.grid[p.y][p.x].isTraversable


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
        if navGrid.inBounds(p) and navGrid.isTraversable(p):
            neighbors.append(p)
    return neighbors


@dataclass
class StateSpace():
    dronePosition: Position
    path: List[Position]
    mustVisitNodes: Set[Position]
    navigationGrid: NavigationGrid  # 2D Array of Position

    def getFCost(self) -> float:
        return self.getGCost() + self.getHCost()

    def getHCost(self) -> float:
        currentMax = 0
        for p in self.mustVisitNodes:
            currentMax = max(
                currentMax, getManhattanDistance(self.dronePosition, p))
        return currentMax

    def getGCost(self) -> int:
        return len(self.path)

    def isGoalState(self) -> bool:
        return len(self.mustVisitNodes) == 0

    def getSuccessors(self) -> List[Self]:
        neighborStates = getNeighbors(self.dronePosition, self.navigationGrid)
        successiveStates = []
        for p in neighborStates:
            newMVNodes = self.mustVisitNodes.copy()
            if p in self.mustVisitNodes:
                newMVNodes.remove(p)
            newPath = self.path.copy()
            newPath.append(p)
            newState = StateSpace(
                p, newPath, newMVNodes, self.navigationGrid)
            successiveStates.append(newState)

        return successiveStates

    def getPath(self) -> List[Position]:
        return self.path

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, StateSpace):
            return self.mustVisitNodes == __o.mustVisitNodes and self.dronePosition == __o.dronePosition
        else:
            return False

    def __lt__(self, other: Self):
        return self.getFCost() < other.getFCost()

    def __hash__(self) -> int:
        return hash(self.dronePosition) + hash(tuple(self.mustVisitNodes))


class PQ(PriorityQueue):
    def contains(self, s: StateSpace):
        return s in self.queue


def shortestPath(startingState: StateSpace) -> List[Position]:
    '''Finds the shortest path, such that all MVNodes are visited, from a starting state using A* search'''
    q = PQ()
    q._put((startingState.getFCost(), startingState))
    visitedStates = set()
    while q._qsize() != 0:
        currentState = q._get()
        assert(isinstance(currentState[1], StateSpace))
        if currentState[1].isGoalState():
            return currentState[1].getPath()
        neighbors = currentState[1].getSuccessors()
        for state in neighbors:
            assert(isinstance(state, StateSpace))
            if not q.contains(state) and not state in visitedStates:
                q._put((state.getFCost(), state))
        visitedStates.add(currentState[1])
    return (0, [])  # No Path found
