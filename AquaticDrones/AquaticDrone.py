from dataclasses import dataclass
from pose import *
from typing import List
from graphics import *
import numpy as np


@dataclass
class AquaticSuperVisorImage(GraphicsObject):
    def __init__(self, x, y):
        GraphicsObject.__init__(self, ["outline", "fill"])
        self.setFill = self.setOutline
        self.x = float(x)
        self.y = float(y)


@dataclass
class AquaticSupervisor():
    """Class representation for the supervisor robot that deploys drones with their own subroutines"""
    position: Position
    dronesList: List[AquaticDrone]


@dataclass
class AquaticDrone():
    """Class representation for an AquaticDrone Robot. The robot understands its pose: Position and Orientation in order to calculate future trajectory"""
    position: Position
    vector: MovementVector
    supervisor: AquaticSupervisor

    def getSupervisorPos(self) -> Position:
        return self.supervisor.position


if __name__ == "__main__":
    print("Ran")
