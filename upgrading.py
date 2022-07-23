from core import Action, GameState, Upgrade, Debris, Tank
import random


def get_updgrade(our_tank : Tank) -> Upgrade:
  if our_tank.fire_rate < 4:
    return Upgrade.FIRE_RATE_UPGRADE

  if our_tank.max_hp < 2:
    return Upgrade.MAX_HP_UPGRADE
  if our_tank.hp_regen < 2:
    return Upgrade.HP_REGEN

  if our_tank.max_hp < 4:
    return Upgrade.MAX_HP_UPGRADE
  if our_tank.hp_regen < 4:
    return Upgrade.HP_REGEN

  if our_tank.speed < 2:
    return Upgrade.SPEED_UPGRADE
  if our_tank.projectile_damage < 2:
    return Upgrade.PROJECTILE_DAMAGE
 
  if our_tank.speed < 4:
    return Upgrade.SPEED_UPGRADE
  if our_tank.projectile_damage < 4:
    return Upgrade.PROJECTILE_DAMAGE
  
  return random.choice([
        Upgrade.SPEED_UPGRADE,
        Upgrade.FIRE_RATE_UPGRADE,
        Upgrade.PROJECTILE_DAMAGE,
        Upgrade.MAX_HP_UPGRADE,
        Upgrade.BODY_DAMAGE_UPGRADE,
        Upgrade.HP_REGEN,
        Upgrade.PROJECTILE_TIME_TO_LIVE
    ])