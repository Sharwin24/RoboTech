from dataclasses import dataclass
from typing import List, Tuple
from graphics import Image


@dataclass
class AquaticDrone():
    """Class representation for an AquaticDrone Robot. The robot understands its pose: Position and Orientation in order to calculate future trajectory"""
    id: int
    position: Tuple[int, int]
    vector: Tuple[float, float]
    image: Image

    def __hash__(self) -> int:
        return hash(id)

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id

    def setAngle(self, theta: float):
        self.vector[1] = theta

    def getSupervisorPos(self) -> Tuple[int, int]:
        return self.supervisor.position

    def withinRangeOfSupervisor(self, range: float) -> bool:
        return abs(self.getSupervisorPos - self.position) <= range


@dataclass
class AquaticSupervisor():
    """Class representation for the supervisor robot that deploys drones with their own subroutines"""
    id: int
    position: Tuple[int, int]
    dronesList: List[AquaticDrone]
    image: Image

    def __hash__(self) -> int:
        return hash(id)

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id

    def addDrone(self, drone: AquaticDrone):
        self.dronesList.append(drone)

    def removeDrone(self, drone: AquaticDrone):
        self.dronesList.remove(drone)
