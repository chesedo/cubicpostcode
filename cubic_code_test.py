from cubic_code import CubicCode
import pytest


def test_get_x_layer():
    c = CubicCode("5")

    assert c.get_x_layer_and_offset() == (1, 5)

    c = CubicCode("3141592653589793238462")

    assert c.get_x_layer_and_offset() == (7_123_793, 381_589_793_238_462)


def test_get_coordinates():
    c = CubicCode("5")

    assert c.get_coordinates() == (-1, -1, 0)

    c = CubicCode("3141592653589793238462")

    assert c.get_coordinates() == (-8_402_969, 9_767_162, -3_561_896)


def test_to_x_coordinate():
    assert CubicCode.to_x_coordinate(1) == 0.5
    assert CubicCode.to_x_coordinate(4) == -1.5
    assert CubicCode.to_x_coordinate(7_123_793) == 3_561_896.5


def test_to_square_radius():
    assert CubicCode.to_square_radius(1) == 1
    assert CubicCode.to_square_radius(4) == 1
    assert CubicCode.to_square_radius(5) == 2
    assert CubicCode.to_square_radius(16) == 2
    assert CubicCode.to_square_radius(381_589_793_238_462) == 9_767_162


def test_to_min_offset():
    assert CubicCode.to_min_offset(1) == 1
    assert CubicCode.to_min_offset(3) == 17
    assert CubicCode.to_min_offset(5) == 65
    assert CubicCode.to_min_offset(9_767_162) == 381_589_735_999_685


def test_to_x_y():
    assert CubicCode.to_z_y(6) == (0, -1)
    assert CubicCode.to_z_y(9) == (2, 0)
    assert CubicCode.to_z_y(11) == (2, 2)
    assert CubicCode.to_z_y(12) == (1, 2)
    assert CubicCode.to_z_y(13) == (0, 2)
    assert CubicCode.to_z_y(15) == (-1, 1)
    assert CubicCode.to_z_y(16) == (-1, 0)

    assert CubicCode.to_z_y(27) == (3, 3)
    assert CubicCode.to_z_y(55) == (0, 4)
    assert CubicCode.to_z_y(62) == (-3, 0)
    assert CubicCode.to_z_y(44) == (4, -3)
    assert CubicCode.to_z_y(17) == (-2, -2)
    assert CubicCode.to_z_y(1) == (0, 0)

    assert CubicCode.to_z_y(381_589_793_238_462) == (-8_402_969, 9_767_162)
