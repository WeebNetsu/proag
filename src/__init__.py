""" 
    This project allows you to auto level in pokemon revolution online.
    How to run:
    - If on Linux, please run as sudo.
    - You have 5 seconds to focus the pokemon window
    - The SPECIFIC route this is coded for is rock tunnel, right before lavender town, where nurse joy is waiting for you in the cave. Stand directly in front of her
    - Do not unfocus the window, press 'q' to stop the program execution
"""

from time import sleep

from src.run import kanto
from src.utils.parser import parse_cmd_input


def main():
    # take all arguments except the file name
    inputs = parse_cmd_input()

    # you have 5 seconds to set up what you need
    for i in range(5, 0, -1):
        print(i)
        sleep(1)

    if inputs["region"] == "kanto":
        kanto.run(inputs["area"])
