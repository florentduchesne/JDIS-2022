import math
import random
from typing import Tuple

from core import Action, GameState, Upgrade, Debris, Tank
import utils
import clustering
import upgrading
import viser

import deplacement


class MyBot:
    """
    Random bot
    """

    def __init__(self, id):
        self.id = id

    def tick(self, state: GameState) -> Action:
        # Program your bot here
        our_tank = utils.get_our_tank(self.id, state)
        destination=utils.random_center_position(state)

        #si peu d'exp, farm l'exp
        if our_tank.upgrade_levels.max_hp < 1:
            clusters = clustering.clustering(state, 20).cluster_centers_
            best_cluster = utils.get_closer_cluster(our_tank, clusters)
            destination = (int(best_cluster[0][0]), int(best_cluster[0][1]))
        
        closer_tank_id, closer_tank_dist = utils.get_closer_tank(our_tank, state)
        closer_debris, closer_debris_dist = utils.get_closer_debris(our_tank, state)
        
        max_range =  utils.get_max_projectile_range(our_tank) * 0.99
        
        #if closer_tank_dist < max_range:
        #target = state.tanks[closer_tank_id].position
        target = viser.viser_tank(our_tank, state.tanks[closer_tank_id])
        if utils.distance(our_tank.position, target) > max_range:
            if closer_debris_dist < max_range:
                target = closer_debris.position
            else:
                target = utils.random_position(state)
        if closer_tank_dist < utils.get_max_projectile_range(state.tanks[closer_tank_id]) * 0.95:
            dest1, dest2 = deplacement.esquive(our_tank, state.tanks[closer_tank_id])
            if utils.distance(our_tank.position, (2500, 2500)) > 300:
                if utils.distance(dest1, (2500, 2500)) > utils.distance(dest2, (2500, 2500)):
                    destination = dest2
                else:
                    destination = dest1
            else:
                destination = dest2

        return Action(
            destination=destination,
            target=target,
            purchase=upgrading.get_upgrade(our_tank)
        )
