import math
from core import Action, GameState, Upgrade, Debris, Tank
from typing import Tuple, List
import random

import utils

def get_temps(our_tank, other_tank):
    dist = utils.distance(our_tank.position, other_tank.position)
    return dist / 20

def viser_tank(our_tank: Tank, other_tank: Tank):
    if other_tank.destination:
        other_dest = other_tank.destination
        other_pos = other_tank.position
        other_speed = other_tank.speed
        deplacement_x = other_dest[0] - other_pos[0]
        deplacement_y = other_dest[1] - other_pos[1]

        other_dist = utils.distance(other_tank.position, other_tank.destination)
        
        temps_pour_tir = get_temps(our_tank, other_tank)
        if other_dist == 0:
            return other_tank.position
        #deplacement de 1000, 10 par tick => 100 ticks
        #dans 50 ticks : 500
        #dist_dans_temps = (other_dist / other_speed) / temps_pour_tir
        cible_x = other_tank.position[0] + ((deplacement_x / other_dist) * other_speed * temps_pour_tir)
        cible_y = other_tank.position[1] + ((deplacement_y / other_dist) * other_speed * temps_pour_tir)
        return int(cible_x), int(cible_y)
        #return other_tank.position
    else:
        return other_tank.position
    

