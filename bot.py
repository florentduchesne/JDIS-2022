import math
import random
from typing import Tuple

from core import Action, GameState, Upgrade, Debris, Tank


class MyBot:
    """
    Random bot
    """

    def __init__(self, id):
        self.id = id

    def random_position(self, state: GameState) -> Tuple[float]:
        x = random.randrange(0, state.map_width)
        y = random.randrange(0, state.map_height)
        return x, y
    def random_center_position(self, state: GameState) -> Tuple[float]:
        x = random.randrange(2000, 3000)
        y = random.randrange(2000, 3000)
        return x, y
    
    def get_our_tank(self, state):
        for key in state.tanks:
            if state.tanks[key].id == self.id:
                return state.tanks[key]
        return None
    
    def distance(self, pos1, pos2):
        dx = abs(pos1[0] - pos2[0])
        dy = abs(pos1[1] - pos2[1])
        return math.sqrt(dx * dx + dy * dy)

    def get_closer_tank(self, state: GameState) -> Tuple[float]:
        min_dist = 5000 * 5000
        min_tank = None
        our_tank = self.get_our_tank(state)
        for key in state.tanks:
            if state.tanks[key].id != self.id:
                pos1 = state.tanks[key].position
                pos2 = our_tank.position
                dist = self.distance(pos1, pos2)
                if min_dist > dist:
                    min_dist = dist
                    min_tank = key
        return min_tank, min_dist

    def random_upgrade(self) -> Upgrade:
        return random.choice([
            Upgrade.SPEED_UPGRADE,
            Upgrade.FIRE_RATE_UPGRADE,
            Upgrade.PROJECTILE_DAMAGE,
            Upgrade.MAX_HP_UPGRADE,
            Upgrade.BODY_DAMAGE_UPGRADE,
            Upgrade.HP_REGEN,
            Upgrade.PROJECTILE_TIME_TO_LIVE
        ])

    def tick(self, state: GameState) -> Action:
        # Program your bot here
        target = self.random_position(state)
        closer_tank_id, closer_tank_dist = self.get_closer_tank(state)
        if closer_tank_dist < 500:
            target = state.tanks[closer_tank_id].position

        return Action(
            destination=self.random_center_position(state),
            target=target,
            purchase=self.random_upgrade()
        )
