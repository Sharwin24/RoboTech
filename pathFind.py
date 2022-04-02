from dataclasses import dataclass
from typing import List
from typing import Tuple
from typing import Set


@dataclass
class Position():
    x: int
    y: int


@dataclass
class Node():
    position: Position
    hasAlgae: bool
    isWall: bool

    def removeAlgae(self):
        self.hasAlgae = False

    def __eq__(self, __o: object) -> bool:
        pass

    def __hash__(self) -> int:
        pass


@dataclass
class StateSpace():
    dronePosition: Position
    path: List[Position]
    mustVisitNodes: Set[Position]
    navigationGrid: List[List[Node]]  # 2D Array of Position

    def isGoalState(self):
        return len(self.mustVisitNodes) == 0

    def __eq__(self, __o: object) -> bool:
        pass

    def __hash__(self) -> int:
        pass


@dataclass
class PathFind():

    def shortestPath(self, startingState: StateSpace) -> List[Position]:
        pass
