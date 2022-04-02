from dataclasses import dataclass


@dataclass
class Position():
    x: int
    y: int


@dataclass
class MovementVector():
    orientation: float
    velocity: float
