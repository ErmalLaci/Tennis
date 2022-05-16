"""Defines the hexes that populate a grid."""
from typing import Tuple


class Hex:
    def __init__(self, x: int, y: int) -> None:
        """Initialise a new hex.

        Parameters:
            x: x axial coordinate.
            y: y axial coordinate.

        """
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        """The x axial coordinate of the hex.

        Returns:
            Coordinate

        """
        return self._x

    @property
    def y(self) -> int:
        """The y axial coordinate of the hex.

        Returns:
            Coordinate

        """
        return self._y

    @property
    def z(self) -> int:
        """The z axial coordinate of the hex.

        Calculated from the x and y coordinates.

        Returns:
            Coordinate

        """
        # TODO: could be better just to calculate this on init
        return # TODO: formula for coordinate generation

    @property
    def axial(self) -> Tuple[int, int, int]:
        """The axial coordinates for the hex centre.

        Return:
            (x, y, z)
        """
        return self.x, self.y, self.z

    @property
    def cartesian(self) -> Tuple[int, int]:
        """The cartesian coordinates for the hex centre.

        Return:
            (x, y)
        """
        return # TODO: formula for coordinate generation
