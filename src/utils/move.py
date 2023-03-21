""" 
Player movement, forwards, backwards, left, right, W-S-A-D
"""

import pyautogui as pya

from src.utils.globals import DEBUG


def move_forward():
    """
    Move player forward
    """
    pya.press("w")

    if DEBUG:
        print("MOVE FORWARDS")


def move_backward():
    """
    Move player backwards
    """
    pya.press("s")

    if DEBUG:
        print("MOVE BACKWARDS")


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
