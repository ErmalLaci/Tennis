"""Defines the grid on which hexes can be generated."""
from typing import Dict, Optional

from tennis.src.models.hex import Hex
from tennis.src.types import AxialCoordinate

# Environment variables
MISSING_GRID_ERROR_MSG = 'A grid must be generated before it can be visualised!'

# Local types
GridMap = Dict[AxialCoordinate, Optional[Hex]]


class Grid:
    def __init__(self) -> None:
        self._grid = None

    @property
    def grid(self) -> GridMap:
        """The collection of hexes representing the grid.

        A grid is a mapping of axial coordinates to hexes (or void spaces).

        Return:
            The grid.
        """
        return self._grid

    @grid.setter
    def grid(self, grid: GridMap) -> None:
        self._grid = grid

    def generate(self, **options) -> None:
        """Use the provided options to generate a grid of hexes.

        Parameters:
            options: Set of options to determine behaviour of grid generation.

        """
        grid = {}

        # TODO: generate...

        self.grid = grid

    def visualise(self) -> None:
        """Produce an image file representing the grid.
        """
        if self.grid is None:
            raise ValueError(MISSING_GRID_ERROR_MSG)
