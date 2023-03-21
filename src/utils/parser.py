""" 
Parse inputs and values from here
"""

import sys

from src.utils.globals import AVAILABLE_AREAS


def parse_cmd_input() -> dict[str, str]:
    # take all arguments except the file name
    arguments = sys.argv[1:]

    if len(arguments) != 2:
        print("Invalid number of arguments provided.")
        print("Example: python __init__.py kanto rock_tunnel")
        exit()

    region = arguments[0]
    if not region in AVAILABLE_AREAS.keys():
        print(f"Region '{region}' is not a valid region.")
        exit()

    area = arguments[1]

    if not area in AVAILABLE_AREAS[region]:
        print(f"Area '{area}' is not a valid area.")
        exit()

    return {
        "region": region,
        "area": area,
    }
