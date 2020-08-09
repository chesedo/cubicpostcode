from typing import Tuple


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
