from time import sleep

from src.utils import check_quit
from src.utils.actions import fight_player, heal_player
from src.utils.globals import AREA_CHANGE_WAIT, DEBUG, STEP_DURATION
from src.utils.move import move_down, move_left, move_right, move_up


def move_player(move_iter: int, step_count: int) -> int:
    """
    Will move the player forward and backwards. Returns true if movement was reset.

    `move_iter` - current loop iteration count of player movement
    """
    if move_iter < (step_count + 15):  # move to the edge of the map
        move_down()
        return 15
    elif move_iter < (step_count + 8):  # 8 steps to the left
        move_left()
        return 8
    elif move_iter < (step_count + 9):  # move to next map (9)
        move_down()

        if move_iter == ((step_count + 9) - 1):
            move_down()
            sleep(AREA_CHANGE_WAIT)

        return 9
    elif move_iter < (step_count + 12):  # 12 steps down
        move_down()
        return 12
    elif move_iter < (step_count + 32):  # go to edge of grass patch (32)
        move_left()
        return 32

        # there are 15 grass patches, 21 blocks total
    elif move_iter < (step_count + 16):  #! assume you have entered a fight here
        move_right()
        return 16
    elif move_iter < (step_count + 29):  # leave grass patch (29)
        move_right()
        return 29
    elif move_iter < (step_count + 1):  # move away from bench
        move_left()
        return 1
    elif move_iter < (step_count + 13):  # 13 steps to new area
        move_left()

        if move_iter == ((step_count + 13) - 1):
            move_up()
            sleep(AREA_CHANGE_WAIT)

        return 13
    elif move_iter < (step_count + 25):  # move up as much as possible (25)
        move_up()
        return 25
    elif move_iter < (step_count + 8):  # move in front of heal area (8)
        move_right()
        return 8
    elif move_iter < (step_count + 2):  # enter building (2)
        move_up()

        if move_iter == ((step_count + 2) - 1):
            move_up()
            sleep(AREA_CHANGE_WAIT)

        return 2
    elif move_iter < (step_count + 10):  #! ask nurse joy to heal (10)
        move_up()
        return 10
    elif move_iter < (step_count + 6):  # move back to starting position (6)
        move_down()

        if move_iter == ((step_count + 2) - 1):
            move_down()
            sleep(AREA_CHANGE_WAIT)

        return 6
    else:
        if DEBUG:
            print("MOVING RESET\n")

    return -1


def run():
    # number of iterations passed (to know when to move forward/backwards)
    num_iter = 0
    step_count = 0

    while True:
        if check_quit():
            break

        step_inc = move_player(num_iter, step_count)
        if step_inc < 0:
            num_iter = 0
            step_count = 0
            continue

        sleep(STEP_DURATION)

        # if potentially in a fight, fight pokemon
        if num_iter == 90 and fight_player():
            break

            # if at nurse joy, heal
        if num_iter == 188:
            heal_player()

        num_iter += 1

        if num_iter == (step_count + step_inc):
            step_count += step_inc

        if DEBUG:
            print(num_iter)
