from dataclasses import dataclass
from typing import List
from typing import Tuple
from typing import Set


@dataclass
class Position():
    x: int
    y: int

    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Position):
            return self.x == __o.x and self.y == __o.y
        else:
            return False

    def __repr__(self) -> str:
        return "[" + str(self.x) + "," + str(self.y) + "]"

<<<<<<< HEAD
def getNeighbors(p: Position, navGrid) -> List[Position]:
=======

<<<<<<< HEAD
=======
def getNeighbors(p: Position, navGrid) -> List[Position]:
    assert(isinstance(p, Position))
>>>>>>> afece7049054a48192e0001dd42fb1c3e810c032
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


>>>>>>> pygameSim
def getManhattanDistance(p1: Position, p2: Position) -> int:
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)


def getEuclideanDistance(p1: Position, p2: Position) -> float:
    return pow(p2.x-p1.x, 2) + pow(p2.y-p1.y, 2)
