#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from cubic_code import CubicCode


def main(args):
    c = CubicCode(args.CubicCode)

    x, y, z = c.get_coordinates()

    print(f"[x, y, z] = [{x}, {y}, {z}]")

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "CubicCode", help="The Cubic Code that will be converted", type=str
    )

    main(parser.parse_args())

