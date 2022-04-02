from dataclasses import dataclass
from typing import List, Tuple
from graphics import Image


# Going to change to an image that we've created
# class AquaticSupervisorImage(_BBox):

#     def __init__(self, p1, p2):
#         _BBox.__init__(self, p1, p2)

#     def __repr__(self):
#         return "AquaticSupervisor({}, {})".format(str(self.p1), str(self.p2))

#     def _draw(self, canvas, options):
#         p1 = self.p1
#         p2 = self.p2
#         x1, y1 = canvas.toScreen(p1.x, p1.y)
#         x2, y2 = canvas.toScreen(p2.x, p2.y)
#         return canvas.create_rectangle(x1, y1, x2, y2, options)

#     def clone(self):
#         other = Rectangle(self.p1, self.p2)
#         other.config = self.config.copy()
#         return other


# class AquaticDroneImage(_BBox):
#     def __init__(self, p1, p2):
#         _BBox.__init__(self, p1, p2)

#     def __repr__(self):
#         return "AquaticDrone({}, {})".format(str(self.p1), str(self.p2))

#     def clone(self):
#         other = Oval(self.p1, self.p2)
#         other.config = self.config.copy()
#         return other

#     def _draw(self, canvas, options):
#         p1 = self.p1
#         p2 = self.p2
#         x1, y1 = canvas.toScreen(p1.x, p1.y)
#         x2, y2 = canvas.toScreen(p2.x, p2.y)
#         return canvas.create_oval(x1, y1, x2, y2, options)


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
