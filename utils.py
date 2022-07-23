import math
from core import Action, GameState, Upgrade, Debris, Tank
from typing import Tuple, List
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

def get_closer_cluster(our_tank: Tank, clusters: List):
    min_dist = 5000*5000
    best_cluster = None
    for cluster in clusters:
        pos1 = our_tank.position
        pos2 = cluster
        dist = distance(pos1, pos2)
        if min_dist > dist:
            min_dist = dist
            best_cluster = cluster
    return best_cluster, min_dist

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

def get_closer_debris(our_tank: Tank, state: GameState) -> Tuple[float]:
    min_dist = 5000 * 5000
    min_debris = None
    for debris in state.debris:
        pos1 = debris.position
        pos2 = our_tank.position
        dist = distance(pos1, pos2)
        if min_dist > dist:
            min_dist = dist
            min_debris = debris
    return min_debris, min_dist

def get_max_projectile_range(tank: Tank) -> float:
    return tank.projectile_time_to_live * 20

def random_position(state: GameState) -> Tuple[float]:
    x = random.randrange(0, state.map_width)
    y = random.randrange(0, state.map_height)
    return x, y
def random_center_position() -> Tuple[float]:
    x = random.randrange(1500, 3500)
    y = random.randrange(1500, 3500)
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
