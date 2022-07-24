from core import Action, GameState, Upgrade, Debris, Tank
import random


def get_upgrade(our_tank : Tank) -> Upgrade:
  if our_tank.upgrade_levels.projectile_damage < 1:
    return Upgrade.PROJECTILE_DAMAGE
  if our_tank.upgrade_levels.fire_rate < 2:
    return Upgrade.FIRE_RATE_UPGRADE

  if our_tank.upgrade_levels.max_hp < 2:
    return Upgrade.MAX_HP_UPGRADE
  if our_tank.upgrade_levels.hp_regen < 2:
    return Upgrade.HP_REGEN

  if our_tank.upgrade_levels.max_hp < 3:
    return Upgrade.MAX_HP_UPGRADE
  if our_tank.upgrade_levels.hp_regen < 3:
    return Upgrade.HP_REGEN

  if our_tank.upgrade_levels.projectile_time_to_live < 2:
    return Upgrade.PROJECTILE_TIME_TO_LIVE
  if our_tank.upgrade_levels.fire_rate < 3:
    return Upgrade.FIRE_RATE_UPGRADE

  if our_tank.upgrade_levels.speed < 2:
    return Upgrade.SPEED_UPGRADE
  if our_tank.upgrade_levels.projectile_damage < 2:
    return Upgrade.PROJECTILE_DAMAGE
 
  if our_tank.upgrade_levels.speed < 3:
    return Upgrade.SPEED_UPGRADE
  if our_tank.upgrade_levels.projectile_damage < 3:
    return Upgrade.PROJECTILE_DAMAGE
  
  return random.choice([
        Upgrade.FIRE_RATE_UPGRADE,
        Upgrade.PROJECTILE_DAMAGE,
        Upgrade.MAX_HP_UPGRADE,
        Upgrade.HP_REGEN,
    ])