import time
from typing import Any

# ----- Game messages & UI -----

def intro_msg() -> None:
    ''' Game start message '''
    print('\n====== Simple RPG Game =====')
    input('\nPress [enter] to start...')
        
def game_complete() -> None:
    ''' Finish game message '''
    print('\n=========================================')
    print('\n                VICTORY                \n')
    print('=========================================')
    print('\nCongratulations! You have cleared the game!')
    print('\n\nThanks for trying Simple RPG!\n')
    print('=========================================')
        
def divider() -> None:
    ''' Divider for visualization '''
    print('\n-----------------------------')

# ----- Combat UI prints -----

def attack_print(attacker: Any, defender: Any, damage: int) -> None:
    ''' Damage print without weapon (player/enemy)'''
    print(f'({attacker.__class__.__name__}) {attacker.name} attacks {defender.name} for {damage} damage!')
    print(f'({defender.__class__.__name__}) {defender.name} remaining HP: {defender.hp}')
    time.sleep(0.8)

def weapon_attack_print(attacker: Any, defender: Any, damage: int, bonus_damage: int) -> None:
    ''' Damage print with equipped weapon (player) (non-crit) '''
    print(f'({attacker.__class__.__name__}) {attacker.name} attacks {defender.name} for a total of {damage}! (Base Power: {attacker.attack_power} + Weapon roll: {bonus_damage})')
    print(f'({defender.__class__.__name__}) {defender.name} remaining HP: {defender.hp}')
    time.sleep(0.8)

def crit_attack_print(attacker: Any, defender: Any, damage: int, crit_damage: int) -> None:
     ''' Damage print for critical strike (player) '''
     print(f'({attacker.__class__.__name__}) {attacker.name} attacks with a critical hit {defender.name} for a total of {damage} damage! (Base Power: {attacker.attack_power} + Weapon roll: {crit_damage}) (CRITICAL HIT)')
     print(f'({defender.__class__.__name__}) {defender.name} remaining HP: {defender.hp}')
     time.sleep(0.8)

def block_print(attacker: Any, defender: Any) -> None:
    ''' Blocking attack print (player)'''
    print(f'({attacker.__class__.__name__}) {attacker.name} attacks {defender.name} but the attack gets blocked! (SUCCESSFUL BLOCK)')
    print(f'({defender.__class__.__name__}) {defender.name} remaining HP: {defender.hp}')
    time.sleep(0.8)