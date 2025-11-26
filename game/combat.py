from game.player import Player
from game.helpers import player_info, get_valid_input
from game.equipments import equip_main_hand, equip_off_hand
from game.enemy import Enemy
from game.enemy_data import common_enemies, elite_enemies, boss
from game.ui import game_complete, divider
from game.serialization import save_game, load_game
from game.item_info import shield_info, weapon_info
from typing import Any
import random
import time

# ----- Combat Functions -----

def decide_turn(player: Any, enemy: Any) -> tuple[Any, Any]:
    ''' Turn decision logic'''
    while True:
        player_input = input('\nType [roll] to roll a dice and see if you attack first: ')
        if player_input.strip().lower() == 'roll':
            player_dice = random.randint(1,6)
            divider()
            print(f'\nYou rolled: {player_dice}!')
        else:
            print('\nWrong choice, please type "roll"')
            continue
        enemy_dice = random.randint(1,6)
        print(f'\nEnemy rolled: {enemy_dice}')
        divider()
        if player_dice > enemy_dice:
            print(f'\nPlayer won and will attack first')
            divider()
            return player, enemy
        elif enemy_dice > player_dice:
            print(f'\nEnemy won and will attack first')
            divider()
            return enemy, player
        elif player_dice == enemy_dice:
            print('\nIts a tie, you need to roll the dice again')
            divider()
            continue

def combat(attacker: Any, defender: Any, player: Any, enemy: Any) -> None:
    ''' Combat logic '''
    round_counter = 0
    get_valid_input('\nPress [x] to see the combat info: ', ['x'])
    player.show_info()
    print('\n      VERSUS')
    enemy.show_info()
    get_valid_input('\nPress [x] to start the combat: ', ['x'])
    print('\n=============================')
    print('\n         COMBAT START        ')
    print('\n=============================')
    while attacker.is_alive() and defender.is_alive():
        round_counter += 1
        print(f'\n---------- Round: {round_counter} ---------\n')
        attacker.attack(defender)
        if defender.is_alive():
            if defender.name == player.name and len(defender.consumables_inventory) > 0 and defender.hp < (round(defender.max_hp * 0.4)):
                divider()
                print(f'\n{defender.name} HP is below 40%, a potion will be used')
                defender.use_potion()
            defender, attacker = attacker, defender
        else:
            print('\n--------- Combat Ended ---------')
            print(f'\n{attacker.name} is victorious!!!')
            if attacker.name != player.name:
                print('\nThe hero has fallen.')
                print('\nGame Over...')
            else:
                player.gain_xp(enemy.exp)
                time.sleep(0.7)

# ----- Main Combat Phase Helpers -----

def combat_loop(player: Any, enemy: Any) -> None:
    ''' Main combat loop '''
    attacker, defender = decide_turn(player, enemy)
    combat(attacker, defender, player, enemy)

def combat_drops(player: Any, enemy: Any, all_enemies: list, i: int) -> None:
    ''' Combat drops post fight '''
    if i < len(all_enemies) - 1:
        if (random.random() < enemy.potion_drop_chance):
            player.consumables_inventory.append('Potion')
            divider()
            print(f'\nHealing Potion dropped (own: {len(player)}). It will be added to your inventory!')
            time.sleep(0.5)
        # Weapon drop and equip / replace
        for weapon, drop_chance in enemy.drop_table:
            if random.random() < drop_chance:
                divider()
                print(f'\nA {weapon.name} dropped. Added to inventory.')
                divider()
                time.sleep(0.5)
                player.weapon_inventory.append(weapon)

                if weapon == player.equipped_weapon or weapon == player.equipped_shield:
                    print('\nThe item is already equipped. Will be added to inventory.')
                    continue
                if weapon.item_type == 'Off-Hand':
                    user_choice = get_valid_input('\nWant to see the Shield Book? (y/n): ',['y','n'])
                    if user_choice == 'y':
                        shield_info()
                        time.sleep(0.3)
                        equip_off_hand(player, weapon)
                    else:
                        divider()
                        equip_off_hand(player, weapon)
                        continue
                elif weapon.item_type == 'Main-Hand':
                    user_choice = get_valid_input('\nWant to see the Weapon Book? (y/n): ',['y','n'])
                    if user_choice == 'y':
                        weapon_info()
                        time.sleep(0.3)
                        equip_main_hand(player, weapon)
                    else:
                        divider()
                        equip_main_hand(player, weapon)
                        continue

def post_fight_hp(player) -> None:
    ''' Post fight alert message'''
    time.sleep(0.4)
    divider()
    print(f'\n[!] ALERT: {player.name} remaining HP: {player.hp}')
    divider()

def post_fight_healing(player) -> None:
    ''' Post fight player healing '''
    if player.hp < player.max_hp and len(player.consumables_inventory) > 0: 
        print(f'\nInventory: {len(player)} Potions left')
        divider()
        potion_user_input = get_valid_input('\nDo you want to use a potion? (y/n): ',['y', 'n'])
        divider()
        if potion_user_input.lower().strip() == 'y':
            print('\nA potion will be used to replenish your HP')
            player.use_potion()
            print(f'Inventory: {len(player)} Potions left')
            divider()
        else:
            return

# Main Menu
def main_menu() -> None:
    print('\n1. New game'
          '\n2. Load Game'
          '\n3. Exit')
    game_menu = get_valid_input('\nEnter Choice: ',['1','2','3'])
    if game_menu == '1':
        start_new_game()
    elif game_menu == '2':
        start_loaded_game()
    else:
        exit()

# New game function
def start_new_game() -> None:
    ''' Starting new game '''
    p_name, p_hp, p_power = player_info()
    player = Player(p_name, p_hp, p_power)
    player.show_info()

    all_enemies = generate_enemies()

    start_combat_loop(player, all_enemies, index=0)

# Load saved game function
def start_loaded_game() -> None:
    ''' Loading saved progress '''
    player, index = load_game()
    player.show_info()
    all_enemies = generate_enemies()
    start_combat_loop(player, all_enemies, index)

# Generate enemy list
def generate_enemies() -> list[Enemy]:
    ''' Generating fixed amount of enemies with randomized position and the final boss '''
    all_enemies = []
    for i in range(7):
        name, hp, power, potion_drop_chance, exp, drop_table = common_enemies()
        all_enemies.append(Enemy(name, hp, power, potion_drop_chance, exp, drop_table))

    for i in range(5):
        name, hp, power, potion_drop_chance, exp, drop_table = elite_enemies()
        all_enemies.append(Enemy(name, hp, power, potion_drop_chance, exp, drop_table))

    random.shuffle(all_enemies)
    boss_stats = boss()
    all_enemies.append(Enemy(*boss_stats))
    return all_enemies

def start_combat_loop(player: Player, all_enemies: list[Enemy], index: int) -> None:
    ''' Main combat loop '''
    for i in range(index, len(all_enemies)):
        enemy = all_enemies[i]

        if not player.is_alive():
            break
        # Dice roll for turn decision
        combat_loop(player, enemy)

        if not player.is_alive():
            break

        if i == len(all_enemies) - 1 and player.is_alive():
            game_complete()
            break

        combat_drops(player, enemy, all_enemies, i)

        post_fight_hp(player)

        post_fight_healing(player)

        user_input = get_valid_input('\nPress [x] to start combat or [s] to save and quit: ',['x','s'])
        divider()
        if user_input == 'x':
            continue
        else:
            save_game(player, i)
            divider()
            print('\nGame Saved!')