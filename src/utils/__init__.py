""" 
General utility functions that can be used in the whole project
"""

import keyboard


def check_quit() -> bool:
    """
    Checks if game loop should be quit (whenever the player presses 'q')
    """
    if keyboard.is_pressed("q"):
        print("Execution quit!")
        return True

    return False
