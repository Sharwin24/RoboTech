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


def getManhattanDistance(p1: Position, p2: Position) -> int:
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)


def getEuclideanDistance(p1: Position, p2: Position) -> float:
    return pow(p2.x-p1.x, 2) + pow(p2.y-p1.y, 2)
