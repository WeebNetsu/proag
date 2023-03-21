""" 
Common actions the player can take that does not change anywhere.
"""

from time import sleep

import pyautogui as pya

from src.utils import check_quit
from src.utils.globals import BANDWIDTH_WAIT, DEBUG, FIGHT_ROUNDS


def fight_player() -> bool:
    """
    Will allow the player to fight `rounds` amount of times.
    Will return true if game loop should be quit early
    """
    if DEBUG:
        print("in fight")

    if check_quit():
        return True

    sleep(BANDWIDTH_WAIT + 4)

    # attack rounds amount of times
    for _ in range(0, FIGHT_ROUNDS):
        if DEBUG:
            print("attack")

        pya.press("1")
        pya.press("1")

        if check_quit():
            return True

        sleep(BANDWIDTH_WAIT + 4)

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
