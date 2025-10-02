import random
from weapons import Dagger, Shortsword

# input validation
def get_valid_input(prompt, options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input not in options:
            print('\nInvalid input, try again')
        else:
            return user_input
        
# valid name
def get_valid_name(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isalpha():
            return user_input
        else:
            print('\nName cannot contain blank spaces, numbers, puncuations. Please type again.')

# player information
def player_info():
    player_name = get_valid_name('\nPlease insert the name of your player: ').capitalize()
    player_hp = random.randint(10,15)
    player_power = random.randint(3,5)
    return player_name, player_hp, player_power

# List of Enemies
def lvl1_enemy():
    enemies = []
    for i in range(2):
        name = 'lvl[1] Goblin Soldier'
        hp = random.randint(3,4)
        power = random.randint(2,3)
        potion_drop_chance = 0.3
        drop_table = [(Dagger, 0.3)]
        enemies.append((name, hp, power, potion_drop_chance, drop_table))
    return enemies

def lvl2_enemy():
    enemies = []
    for i in range(2):
        name = 'lvl[2] Goblin Grunt'
        hp = random.randint(4,5)
        power = random.randint(3,4)
        potion_drop_chance = 0.4
        drop_table = [(Shortsword, 0.25)]
        enemies.append((name, hp, power, potion_drop_chance, drop_table))
    return enemies

def boss():
    name = 'Goblin Captain'
    hp = 8
    power = 5
    potion_drop_chance = 0
    drop_table = 0
    return name, hp, power, potion_drop_chance, drop_table

# Who attacks first
def decide_turn(player, enemy):
    while True:
        player_input = input('\nType "roll" to roll a dice and see if you attack first: ')
        if player_input.strip().lower() == 'roll':
            player_dice = random.randint(1,6)
            print(f'\nYou rolled: {player_dice}!')
        else:
            print('\nWrong choice, please type "roll"')
            continue
        enemy_dice = random.randint(1,6)
        print(f'Enemy rolled: {enemy_dice}\n')
        if player_dice > enemy_dice:
            (print(f'Player won and will attack first\n'))
            return player, enemy
        elif enemy_dice > player_dice:
            print(f'Enemy won and will attack first\n')
            return enemy, player
        elif player_dice == enemy_dice:
            print('Its a tie, u need to roll the dice again')
            continue

# Combat mode
def combat(attacker, defender, player, enemy):
    round_counter = 0
    combat_info = get_valid_input('\nPress x to see the combat info: ', ['x'])
    player.show_info()
    print('\nversus')
    enemy.show_info()
    combat_start = get_valid_input('\nPress x to start the combat: ', ['x'])
    while attacker.is_alive() and defender.is_alive():
        round_counter += 1
        print(f'\n-- Round: {round_counter} --\n')
        attacker.attack(defender)
        if defender.is_alive():
            if defender.name == player.name and len(defender.consumables_inventory) > 0 and defender.hp < (round(defender.max_hp * 0.7)):
                print(f'\n{defender.name} HP is below 30%, a potion will be used')
                defender.use_potion()
            defender, attacker = attacker, defender
        else:
            print('\n--- Combat Ended ---')
            print(f'\n{attacker.name} is victorious!!!')
            if attacker.name != player.name:
                print('\nThe hero has fallen.')
                print('\nGame Over...')