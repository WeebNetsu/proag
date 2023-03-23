from src.utils import check_quit
from src.utils.actions import fight_player, heal_player
from src.utils.globals import DEBUG
from src.utils.move import move_down, move_up


def move_player(move_iter: int) -> bool:
    """
    Will move the player forward and backwards. Returns true if movement was reset.

    `move_iter` - current loop iteration count of player movement
    """
    if move_iter < 30:
        move_down()
    elif move_iter < 60:
        move_up()
    elif move_iter < 90:
        move_down()
    elif move_iter < 120:
        move_up()
    else:
        if DEBUG:
            print("MOVING RESET\n")

        return True

    return False


def run():
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
        if num_iter == 119 and fight_player():
            break

            # if at nurse joy, heal
        if num_iter == 29:
            heal_player()

        num_iter += 1

        if DEBUG:
            print(num_iter)
