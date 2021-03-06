from typing import Tuple
import math


class CubicCode:
    def __init__(self, code: str) -> None:
        """Create a CubicCode class

        Args:
            code (str): The cubic code to use
        """
        self.__code = int(code)

    def get_x_layer_and_offset(self) -> Tuple[int, int]:
        """Get the x-layer and offset for the cubic code

        Returns:
            Tuple[int, int]: The x-layer number and offset number of the cubic code
        """
        q, r = divmod(self._CubicCode__code, 441_000_000_000_000)

        if r == 0:
            return (q, 441_000_000_000_000)

        return (q + 1, r)

    def get_coordinates(self) -> Tuple[int, int, int]:
        """Get the co-ordinates of this CubicCode

        Returns:
            Tuple[int, int, int]: The x, y and z co-ordinates
        """
        l, o = self.get_x_layer_and_offset()

        x = CubicCode.to_x_coordinate(l)
        (y, z) = CubicCode.to_y_z(o)

        return (x, y, z)

    @staticmethod
    def to_x_coordinate(layer: int) -> float:
        """Convert the x-layer number to the x co-ordinate

        Args:
            layer (int): The layer number to convert

        Returns:
            float: X co-ordinate for the layer number
        """
        q, r = divmod(layer, 2)

        if r == 1:
            return q + 0.5

        return -(q - 0.5)

    @staticmethod
    def to_square_radius(offset: int) -> int:
        """Convert an offset to its square radius

        Args:
            offset (int): The offset to convert

        Returns:
            int: The square radius the offset is in
        """
        return math.ceil(math.sqrt(offset) / 2)

    @staticmethod
    def to_min_offset(radius: int) -> int:
        """Calculate the minimum offset for a radius

        Args:
            radius (int): The square radius

        Returns:
            int: The minimum offset in the square radius
        """
        return (2 * (radius - 1)) ** 2 + 1

    @staticmethod
    def to_y_z(offset: int) -> Tuple[int, int]:
        """Calculate the y and z from a x-layer offset

        Args:
            offset (int): The offset

        Returns:
            Tuple[int, int]: The calculated y and z co-ordinates
        """
        r = CubicCode.to_square_radius(offset)
        mini = CubicCode.to_min_offset(r)
        length = 2 * r - 1

        offset -= mini

        # In top row
        if offset < length:
            return (offset - r + 0.5, r - 0.5)

        offset -= length

        # In right row
        if offset < length:
            return (r - 0.5, -(offset - r) - 0.5)

        offset -= length

        # In bottom row
        if offset < length:
            return (-(offset - r) - 0.5, -r + 0.5)

        offset -= length

        # In left row
        return (-r + 0.5, offset - r + 0.5)
