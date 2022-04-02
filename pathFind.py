from dataclasses import dataclass
from typing import List
from typing import Tuple
from typing import Set
from utility import *


@dataclass
class NavigationGrid():
    grid: List[List[Node]]
    width: int
    height: int

    def inBounds(p: Position) -> bool:
        pass


@dataclass
class Node():
    position: Position
    hasAlgae: bool
    isWall: bool

    def removeAlgae(self):
        self.hasAlgae = False

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Node):
            return self.position == __o.position and self.hasAlgae == __o.hasAlgae and self.isWall == __o.isWall
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.position) + hash(self.hasAlgae) + hash(self.isWall)


@dataclass
class StateSpace():
    dronePosition: Position
    path: List[Position]
    mustVisitNodes: Set[Position]
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
        pass

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


@dataclass
class PathFind():
    def shortestPath(self, startingState: StateSpace) -> List[Position]:
        '''Finds the shortest path from a starting state using A* search'''
        pass
