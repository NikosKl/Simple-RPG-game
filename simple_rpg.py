from simple_rpg_helpers import player_info, lvl1_enemy, lvl2_enemy, boss, decide_turn, combat, get_valid_input
from weapons import Dagger, Shortsword
import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    # attack / damage method
    def attack(self, target):
        attacker = self.__class__.__name__
        defender = target.__class__.__name__

        damage = self.attack_power

        if isinstance(self, Player) and player.equipped_weapon:
            min_damage, max_damage = self.equipped_weapon.weapon_damage
            bonus_damage = random.randint(min_damage, max_damage)
            damage += bonus_damage
            target.hp -= damage
            print(f'({attacker}) {self.name} attacks {target.name} for {self.attack_power} and {bonus_damage} as bonus weapon damage!')
            print(f'({defender}) {target.name} remaining HP: {target.hp}')
        else:
            target.hp -= self.attack_power
            print(f'({attacker}) {self.name} attacks {target.name} for {damage} damage!')
            print(f'({defender}) {target.name} remaining HP: {target.hp}')
        if target.hp <= 0:
            target.hp = 0

    def is_alive(self):
        return self.hp > 0

    # Pulling information
    def show_info(self):
        character_type = self.__class__.__name__
        print(f'\n{character_type} Sheet\n'.upper())
        print(f'Name: {self.name}')
        print(f'HP: {self.hp}')
        print(f'Attack Power: {self.attack_power}')
        
class Player(Character):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.consumables_inventory = ['Potion', 'Potion', 'Potion']
        self.max_hp = hp
        self.equipped_weapon = None
        self.weapon_inventory = []

    # inventory space
    def __len__(self):
        return len(self.consumables_inventory)
    
    # potion usage
    def use_potion(self):
        if 'Potion' in self.consumables_inventory:
            heal_amount = round(self.max_hp * 0.3)
            self.hp += heal_amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f'You got healed for {heal_amount} HP by using a Potion!')
            player.consumables_inventory.remove('Potion')
        else:
            print('There is no Potions in the inventory...')

    # weapon equip
    def equip_weapon(self, weapon):
            self.equipped_weapon = weapon
            print(f'\n{weapon.name} has been equipped!')
class Enemy(Character):
    def __init__(self, name, hp, attack_power, potion_drop_chance, drop_table=None):
        super().__init__(name, hp, attack_power)
        self.potion_drop_chance = potion_drop_chance
        self.drop_table = drop_table

# Character info
p_name, p_hp, p_power = player_info()
player = Player(p_name, p_hp, p_power)
player.show_info()
print(f'Inventory: {len(player)} Potions')

# Enemies
all_enemies = []

lvl1_stats = lvl1_enemy()
all_enemies.extend([Enemy(name, hp, power, potion_drop_chance, drop_table) for (name, hp, power, potion_drop_chance, drop_table) in lvl1_stats])

lvl2_stats = lvl2_enemy()
all_enemies.extend([Enemy(name, hp, power, potion_drop_chance, drop_table) for (name, hp, power, potion_drop_chance, drop_table) in lvl2_stats])

boss_stats = boss()
all_enemies.append(Enemy(*boss_stats))

# Combat phase
for i, enemy in enumerate(all_enemies):
    if not player.is_alive():
        break
    # Dice roll for turn decision
    attacker, defender = decide_turn(player, enemy)
    # combat
    combat(attacker, defender, player, enemy)

    if not player.is_alive():
        break
    # Drops & Potion usage post fight
    if i < len(all_enemies) - 1:
        if (random.random() < enemy.potion_drop_chance):
            player.consumables_inventory.append('Potion')
            print(f'\nThe creature dropped a Healing Potion(own: {len(player)}). It will be added to your inventory!')
        # Weapon drop and equip / replace
        for weapon, drop_chance in enemy.drop_table:
            if random.random() < drop_chance:
                print(f'\nThe creature dropped a {weapon.name}, it will be added in your inventory.')
                player.weapon_inventory.append(weapon)
                if player.equipped_weapon is None:
                    print('You dont have any weapon equipped, so it will automatically get equipped!')
                    player.equip_weapon(weapon)
                else: 
                    weapon_equip_input = get_valid_input('\nDo you want to equip the weapon? (y/n): ',['y','n'])
                    if weapon_equip_input.strip().lower() == 'y':
                        player.equip_weapon(weapon)
                    else:
                        continue
        # post fight preparation for next level
        print(f'\nALERT!: {player.name} remaining HP: {player.hp}')
        if player.hp < player.max_hp and len(player.consumables_inventory) > 0: 
            print(f'\nInventory: {len(player)} Potions left')
            potion_user_input = get_valid_input('\nDo you want to use a potion? (y/n): ',['y', 'n'])
            if potion_user_input.lower().strip() == 'y':
                print('\nA potion will be used to replenish your hp')
                player.use_potion()
                print(f'Inventory: {len(player)} Potions left')
            else:
                continue