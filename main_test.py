from main import CubicCode
import pytest


def test_get_z_layer():
    c = CubicCode("5")

    assert c.get_z_layer_and_offset() == (1, 5)

    c = CubicCode("3141592653589793238462")

    assert c.get_z_layer_and_offset() == (7_123_793, 381_589_793_238_462)


def test_to_z_coordinate():
    assert CubicCode.to_z_coordinate(1) == 0
    assert CubicCode.to_z_coordinate(4) == 2
    assert CubicCode.to_z_coordinate(7_123_793) == -3_561_896
