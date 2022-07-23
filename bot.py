import math
import random
from typing import Tuple

from core import Action, GameState, Upgrade, Debris, Tank
import utils
import clustering


class MyBot:
    """
    Random bot
    """

    def __init__(self, id):
        self.id = id

    def tick(self, state: GameState) -> Action:
        # Program your bot here
        our_tank = utils.get_our_tank(self.id, state)
        target = utils.random_position(state)
        destination=utils.random_center_position()

        #si peu d'exp, farm l'exp
        if our_tank.experience < 1000:
            clusters = clustering.clustering(state, 6).cluster_centers_
            best_cluster = utils.get_closer_cluster(our_tank, clusters)
            destination = (int(best_cluster[0][0]), int(best_cluster[0][1]))
            
        
        closer_tank_id, closer_tank_dist = utils.get_closer_tank(our_tank, state)
        if closer_tank_dist < utils.get_max_projectile_range(our_tank) * 0.9:
            target = state.tanks[closer_tank_id].position

        return Action(
            destination=destination,
            target=target,
            purchase=utils.random_upgrade()
        )
