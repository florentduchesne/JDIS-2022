import math
import random
from typing import Tuple

from core import Action, GameState, Upgrade, Debris, Tank
import utils


class MyBot:
    """
    Random bot
    """

    def __init__(self, id):
        self.id = id

    def tick(self, state: GameState) -> Action:
        # Program your bot here
        target = utils.random_position(state)
        
        our_tank = utils.get_our_tank(self.id, state)
        closer_tank_id, closer_tank_dist = utils.get_closer_tank(our_tank, state)
        if closer_tank_dist < 500:
            target = state.tanks[closer_tank_id].position

        return Action(
            destination=utils.random_center_position(),
            target=target,
            purchase=utils.random_upgrade()
        )
