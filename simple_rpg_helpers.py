import random

# player information
def player_info():
    player_name = input('\nPlease insert the name of your player: ').capitalize()
    player_hp = random.randint(10,15)
    player_power = random.randint(3,5)
    return player_name, player_hp, player_power

# enemy information
def enemy_info():
    enemy_name = 'lvl[1] Goblin'
    enemy_hp = random.randint(12,15)
    enemy_power = random.randint(3,4)
    return enemy_name, enemy_hp, enemy_power

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

def combat(attacker, defender, player, enemy):
    round_counter = 0
    #combat_info = input('\nPress x to start the combat: ')
    #if combat_info.lower() == 'x':
    player.show_info()
    print('\nversus\n')
    enemy.show_info()
    combat_start = input('\nPress x to start the combat: ')
    if combat_start.lower() == 'x':
        while attacker.is_alive() and defender.is_alive():
            round_counter += 1
            print(f'\n-- Round: {round_counter} --\n')
            attacker.attack(defender)
            if defender.is_alive():
                defender, attacker = attacker, defender
            else:
                print('\n--- Combat Ended ---')
                print(f'\n{attacker.name} is victorious!!!')
                if attacker.name == player.name:
                    print(f'\nALERT!: {attacker.name} remaining HP: {attacker.hp}')
                    return attacker
                else:
                    print('Game Over...')
    else:
        print('Wrong input, Please type "x".')