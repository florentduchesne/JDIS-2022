import math
from core import Action, GameState, Upgrade, Debris, Tank
from typing import Tuple
import random

def get_our_tank(our_id: int, state: GameState) -> Tank:
    for key in state.tanks:
        if state.tanks[key].id == our_id:
            return state.tanks[key]
    return None

def distance(pos1, pos2):
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return math.sqrt(dx * dx + dy * dy)

def get_closer_tank(our_tank: Tank, state: GameState) -> Tuple[float]:
    min_dist = 5000 * 5000
    min_tank = None
    for key in state.tanks:
        if state.tanks[key].id != our_tank.id:
            pos1 = state.tanks[key].position
            pos2 = our_tank.position
            dist = distance(pos1, pos2)
            if min_dist > dist:
                min_dist = dist
                min_tank = key
    return min_tank, min_dist

def random_position(state: GameState) -> Tuple[float]:
    x = random.randrange(0, state.map_width)
    y = random.randrange(0, state.map_height)
    return x, y
def random_center_position() -> Tuple[float]:
    x = random.randrange(2000, 3000)
    y = random.randrange(2000, 3000)
    return x, y

def random_upgrade() -> Upgrade:
    return random.choice([
        Upgrade.SPEED_UPGRADE,
        Upgrade.FIRE_RATE_UPGRADE,
        Upgrade.PROJECTILE_DAMAGE,
        Upgrade.MAX_HP_UPGRADE,
        Upgrade.BODY_DAMAGE_UPGRADE,
        Upgrade.HP_REGEN,
        Upgrade.PROJECTILE_TIME_TO_LIVE
    ])