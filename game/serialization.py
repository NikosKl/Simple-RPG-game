import json
import os
from typing import Any
from game.weapons import create_weapon
from game.player import Player

def player_dict(player: Player) -> dict[str, Any]:
   return {
      'level': player.lvl,
      'name': player.name,
      'hp': player.hp,
      'max_hp': player.max_hp,
      'attack_power': player.attack_power,
      'exp': player.exp,
      'exp_to_next_lvl': player.exp_to_next_lvl,
      'consumables': player.consumables_inventory,
      'equipped_weapon': player.equipped_weapon.name if player.equipped_weapon else None,
      'equipped_shield': player.equipped_shield.name if player.equipped_shield else None,
      'weapon_inventory': [item.name for item in player.weapon_inventory]
   }

def save_game(player: Player, current_index: int) -> object | int:
   save_data = {
      'player': player_dict(player),
      'enemy_index': current_index
   }
   with open('save_game.json', 'w') as fopen:
    json.dump(save_data, fopen, indent=4)
    print('\nGame has been saved!')
    exit()

def load_game() -> tuple | None:
    if not os.path.exists('save_game.json'):
       print("\nSave not found")
       return None
    try:
        with open('save_game.json', 'r') as saved_data:
           data = json.load(saved_data)
    except: 
        print('\nData cannot be loaded')
        return None
    
    player_data = data['player']

    player = Player(player_data['name'], player_data['max_hp'], player_data['attack_power'])

    player.lvl = player_data['level']
    player.hp = player_data['hp']
    player.exp = player_data['exp']
    player.exp_to_next_lvl = player_data['exp_to_next_lvl']
    player.consumables_inventory = player_data['consumables']
    
    equipped_weapon = player_data['equipped_weapon']
    equipped_shield = player_data['equipped_shield']
    weapon_inventory = player_data['weapon_inventory']
       
    player.equipped_weapon = create_weapon(equipped_weapon)
    player.equipped_shield = create_weapon(equipped_shield)
    player.weapon_inventory = [create_weapon(weapon) for weapon in weapon_inventory]

    enemy_index = data['enemy_index']

    return player, enemy_index
