from cubic_code import CubicCode
import pytest


def test_get_x_layer():
    c = CubicCode("5")

    assert c.get_x_layer_and_offset() == (1, 5)

    c = CubicCode("3141592653589793238462")

    assert c.get_x_layer_and_offset() == (7_123_793, 381_589_793_238_462)

    c = CubicCode("441_000_000_000_000")

    assert c.get_x_layer_and_offset() == (1, 441_000_000_000_000)


def test_get_coordinates():
    c = CubicCode("5")

    assert c.get_coordinates() == (0.5, -1.5, 1.5)

    c = CubicCode("3141592653589793238462")

    assert c.get_coordinates() == (3_561_896.5, -8_402_969.5, -9_767_161.5)


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


def test_to_y_z():
    assert CubicCode.to_y_z(6) == (-0.5, 1.5)
    assert CubicCode.to_y_z(9) == (1.5, 0.5)
    assert CubicCode.to_y_z(11) == (1.5, -1.5)
    assert CubicCode.to_y_z(12) == (0.5, -1.5)
    assert CubicCode.to_y_z(13) == (-0.5, -1.5)
    assert CubicCode.to_y_z(15) == (-1.5, -0.5)
    assert CubicCode.to_y_z(16) == (-1.5, 0.5)

    assert CubicCode.to_y_z(27) == (2.5, -2.5)
    assert CubicCode.to_y_z(55) == (-0.5, -3.5)
    assert CubicCode.to_y_z(62) == (-3.5, 0.5)
    assert CubicCode.to_y_z(44) == (3.5, 3.5)
    assert CubicCode.to_y_z(17) == (-2.5, 2.5)
    assert CubicCode.to_y_z(1) == (-0.5, 0.5)

    assert CubicCode.to_y_z(381_589_793_238_462) == (-8_402_969.5, -9_767_161.5)
