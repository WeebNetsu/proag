""" 
Player movement, forwards, backwards, left, right, W-S-A-D
"""

import pyautogui as pya

from src.utils.globals import DEBUG


def move_up():
    """
    Move player up
    """
    pya.press("w")

    if DEBUG:
        print("MOVE UP")


def move_down():
    """
    Move player down
    """
    pya.press("s")

    if DEBUG:
        print("MOVE DOWN")


def move_left():
    """
    Move player left
    """
    pya.press("a")

    if DEBUG:
        print("MOVE LEFT")


def move_right():
    """
    Move player right
    """
    pya.press("d")

    if DEBUG:
        print("MOVE RIGHT")
