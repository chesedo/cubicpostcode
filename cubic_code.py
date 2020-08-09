from typing import Tuple
import math


class CubicCode:
    def __init__(self, code: str) -> None:
        """Create a CubicCode class

        Args:
            code (str): The cubic code to use
        """
        self.__code = int(code)

    def get_z_layer_and_offset(self) -> Tuple[int, int]:
        """Get the z-layer and offset for the cubic code

        Returns:
            Tuple[int, int]: The z-layer number and offset number of the cubic code
        """
        q, r = divmod(self._CubicCode__code, 441_000_000_000_000)
        return (q + 1, r)

    def get_coordinates(self) -> Tuple[int, int, int]:
        """Get the co-ordinates of this CubicCode

        Returns:
            Tuple[int, int, int]: The x, y and z co-ordinates
        """
        l, o = self.get_z_layer_and_offset()

        z = CubicCode.to_z_coordinate(l)
        (x, y) = CubicCode.to_x_y(o)

        return (x, y, z)

    @staticmethod
    def to_z_coordinate(layer: int) -> int:
        """Convert the z-layer number to the z co-ordinate

        Args:
            layer (int): The layer number to convert

        Returns:
            int: Z co-ordinate for the layer number
        """
        q, r = divmod(layer, 2)

        if r == 0:
            return q

        return -q

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
    def to_x_y(offset: int) -> Tuple[int, int]:
        """Calculate the x and y from a z-layer offset

        Args:
            offset (int): The offset

        Returns:
            Tuple[int, int]: The calculated x and y co-ordinates
        """
        r = CubicCode.to_square_radius(offset)
        mini = CubicCode.to_min_offset(r)
        length = 2 * r - 1

        offset -= mini

        if offset < length:
            return (offset - r + 1, -r + 1)

        offset -= length

        if offset < length:
            return (r, offset - r + 1)

        offset -= length

        if offset < length:
            return (-(offset - r), r)

        offset -= length

        return (-r + 1, -(offset - r))
