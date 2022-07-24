import math
from core import Action, GameState, Upgrade, Debris, Tank
from typing import Tuple, List
import random

def get_vector(pos1, pos2):
    #45 - 0, 15 - 0
    return [pos1[0] - pos2[0], pos1[1] - pos2[1]]

def esquive(our_tank: Tank, other_tank: Tank):
    our_pos = our_tank.position
    other_pos = other_tank.position
    vecteur = get_vector(our_pos, other_pos)
    new_pos1 = (our_pos[0] - vecteur[1], our_pos[1] + vecteur[0])
    new_pos2 = (our_pos[0] + vecteur[1], our_pos[1] - vecteur[0])
    return new_pos1, new_pos2
    