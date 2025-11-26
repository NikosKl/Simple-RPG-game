import time
from game.helpers import get_valid_input
from typing import Any

# ----- Item equipping -----

def equip_off_hand(player, weapon) -> None:
    ''' Off-Hand '''
    if player.equipped_shield is None:
        print('\nYou dont have an off-hand, shield will automatically get equipped!')
        player.equip_shield(weapon)
        time.sleep(0.3)
    else:
        shield_equip_input = get_valid_input('\nDo you want to equip the shield? (y/n): ',['y','n'])
        if shield_equip_input.strip().lower() == 'y':
            player.equip_shield(weapon)

def equip_main_hand(player, weapon) -> None:
    ''' Main-Hand'''
    if player.equipped_weapon is None:
        print('\nYou dont have a main-hand, weapon will automatically get equipped!')
        player.equip_weapon(weapon)
        time.sleep(0.3)
    else:
        weapon_equip_input = get_valid_input('\nDo you want to equip the weapon? (y/n): ',['y','n'])
        if weapon_equip_input.strip().lower() == 'y':
            player.equip_weapon(weapon)