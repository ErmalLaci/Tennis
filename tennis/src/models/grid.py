"""Defines the grid on which hexes can be generated."""


MISSING_GRID_ERROR_MSG = 'A grid must be generated before it can be visualised!'


class Grid:
    def __init__(self) -> None:
        self._grid = None

    @property
    def grid(self):
        return self._grid

    def generate(self, **options) -> None:
        """Use the provided options to generate a grid of hexes.

        Parameters:
            options: Set of options to determine behaviour of grid generation.

        """
        pass

    def visualise(self) -> None:
        """Produce an image file representing the grid.
        """
        if self.grid is None:
            raise ValueError(MISSING_GRID_ERROR_MSG)
