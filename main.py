""" 
    This project allows you to auto level in pokemon revolution online.
    How to run:
    - If on Linux, please run as sudo.
    - You have 5 seconds to focus the pokemon window
    - The SPECIFIC route this is coded for is rock tunnel, right before lavender town, where nurse joy is waiting for you in the cave. Stand directly in front of her
    - Do not unfocus the window, press 'q' to stop the program execution
"""

from time import sleep

import cv2
import keyboard
import pyautogui as pya
from PIL import Image
from pytesseract import pytesseract

# if true, debugging info will be printed to the terminal
DEBUG = True
# number of seconds to wait before interacting with something (change if you have slow internet)
BANDWIDTH_WAIT = 1


def check_quit() -> bool:
    """
    Checks if game loop should be quit (whenever the player presses 'q')
    """
    if keyboard.is_pressed("q"):
        print("Execution quit!")
        return True

    return False


def move_player(move_iter: int) -> bool:
    """
    Will move the player forward and backwards. Returns true if movement was reset.

    `move_iter` - current loop iteration count of player movement
    """
    if move_iter < 30:
        pya.press("s")

        if DEBUG:
            print("S")
    elif move_iter < 60:
        pya.press("w")

        if DEBUG:
            print("W")
    elif move_iter < 90:
        pya.press("s")

        if DEBUG:
            print("S")
    elif move_iter < 120:
        pya.press("w")

        if DEBUG:
            print("W")
    else:
        if DEBUG:
            print("RESET")

        return True

    return False


def fight_player(rounds: int = 4) -> bool:
    """
    Will allow the player to fight `rounds` amount of times.
    Will return true if game loop should be quit early
    """
    if DEBUG:
        print("in fight")

    if check_quit():
        return True

    sleep(BANDWIDTH_WAIT + 3)

    # attack rounds amount of times
    for _ in range(0, rounds):
        if DEBUG:
            print("attack")

        pya.press("1")
        pya.press("1")

        if check_quit():
            return True

        sleep(BANDWIDTH_WAIT + 3)

    if DEBUG:
        print("out fight")

    return False


def heal_player():
    """
    Will interact with nurse Joy to heal pokemon
    """
    if DEBUG:
        print("healing")

    pya.press("space")
    sleep(BANDWIDTH_WAIT)
    pya.press("space")
    sleep(BANDWIDTH_WAIT)
    pya.press("1")
    sleep(BANDWIDTH_WAIT)
    pya.press("space")
    sleep(BANDWIDTH_WAIT)
    pya.press("space")
    # sleep(BANDWIDTH_WAIT)
    # pya.press("space")

    if DEBUG:
        print("out healing")


def main():
    # number of iterations passed (to know when to move forward/backwards)
    # set it to 30 to start walking up, 0 to start walking down
    num_iter = 0

    while True:
        if check_quit():
            break

        if move_player(num_iter):
            num_iter = 0
            continue

        # if potentially in a fight, fight pokemon
        if num_iter == 119 and fight_player(4):
            break

            # if at nurse joy, heal
        if num_iter == 29:
            heal_player()

        num_iter += 1

        if DEBUG:
            print(num_iter)


if __name__ == "__main__":
    # you have 5 seconds to set up what you need
    for i in range(5, 0, -1):
        print(i)
        sleep(1)

    image = pya.screenshot()
    # img = cv2.resize(image, None, fx=2, fy=2)
    text: str = pytesseract.image_to_string(image)
    print("nurse joy" in text.lower())
    print(text[:-1])
    # main()
