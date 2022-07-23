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
        closer_debris, closer_debris_dist = utils.get_closer_debris(our_tank, state)
        
        max_range =  utils.get_max_projectile_range(our_tank) * 0.9
        
        if closer_tank_dist < max_range:
            target = state.tanks[closer_tank_id].position
        elif closer_debris_dist < max_range:
            target = closer_debris.position

        return Action(
            destination=utils.random_center_position(),
            target=target,
            purchase=utils.random_upgrade()
        )
