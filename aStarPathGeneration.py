from typing import List, Set

from pathFind import NavigationGrid
from utility import Position


def getADronesQuadrantGrid(numTotalDrones: int, droneID: int, fullNavGrid: NavigationGrid) -> NavigationGrid:
    '''Given a max number of drones and a specific drone within the range [0 totalDrones] as well as the grid the drone exists on, a quadrant will be created that defines this drones navigationGrid. Will return a the same size navigation grid with any nodes out of range of this drone marked as Non-Traversable'''
    return fullNavGrid # Not implemented yet


def getMVNodeSetFromGrid(navGrid: NavigationGrid) -> Set[Position]:
    MVNodes = set()
    g = navGrid.grid
    for l in g:
        for n in l:
            if n.isMustVisitNode:
                MVNodes.add(n)
