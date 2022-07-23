import math
from core import Action, GameState, Upgrade, Debris, Tank
from typing import Tuple
import random
from sklearn.cluster import KMeans

def clustering(state: GameState, n: int):
    positions = [deb.position for deb in state.debris]
    weights = [deb.max_hp for deb in state.debris]
    return KMeans(n_clusters=15, max_iter=5).fit(positions, sample_weight=weights)
