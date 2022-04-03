from dataclasses import dataclass
from turtle import position, width
from typing import List
from typing import Tuple
from typing import Set
from utility import *


@dataclass
class NavigationGrid():
    grid: List[List[Node]]

    def inBounds(self, p: Position) -> bool:
        height = len(self.grid)
        width = len(self.grid[0])  # Assuming a 2D Matrix
        return p.x >= 0 and p.x < width and p.y >= 0 and p.y < height

    def isWall(self, p: Position) -> bool:
        return self.grid[p.y][p.x].isWall


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


@dataclass
class StateSpace():
    position: Position
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

    def getSuccessors(self) -> List[StateSpace]:
        neighborStates = getNeighbors(self.position, self.navigationGrid)
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
            return self.mustVisitNodes == __o.mustVisitNodes and self.position == __o.position
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.position) + hash(self.mustVisitNodes)


@dataclass
class PathFind():
    def shortestPath(self, startingState: StateSpace) -> List[Position]:
        '''Finds the shortest path from a starting state using A* search'''
        pass
