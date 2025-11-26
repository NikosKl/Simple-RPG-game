import random, time
from tabulate import tabulate
from game.ui import weapon_attack_print, attack_print, crit_attack_print, block_print, divider
from game.helpers import apply_damage

class Character:
    def __init__(self, name: str, hp: int, attack_power: int) -> None:
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    # Attack / Damage method
    def attack(self, target) -> None:
        ''' Function for attacking and dealing damage '''
        damage = self.attack_power
        if isinstance(self, Player):
            if self.equipped_weapon:
                min_damage, max_damage = self.equipped_weapon.weapon_damage
                bonus_damage = random.randint(min_damage, max_damage)
                if random.random() < self.equipped_weapon.crit_chance:
                    crit_damage = bonus_damage * self.equipped_weapon.crit_modifier
                    damage += crit_damage
                    apply_damage(target, damage)
                    crit_attack_print(self, target, damage, crit_damage)
                else:
                    damage += bonus_damage
                    apply_damage(target,damage)
                    weapon_attack_print(self, target, damage, bonus_damage)
            else:
                apply_damage(target, damage)
                attack_print(self, target, damage)
        elif isinstance(target, Player):
            if target.equipped_shield:
                if random.random() < target.equipped_shield.block_chance:
                    block_print(self, target)
                else:
                    apply_damage(target, damage)
                    attack_print(self, target, damage)
            else:
                apply_damage(target, damage)
                attack_print(self, target, damage)

    # Character being alive check
    def is_alive(self) -> bool:
        return self.hp > 0

    # Pulling information
    def show_info(self) -> None:
        ''' Showing information for player and enemies '''
        character_type = self.__class__.__name__
        if isinstance(self, Player):
            main_hand = self.equipped_weapon.name if self.equipped_weapon else 'None'
            off_hand = self.equipped_shield.name if self.equipped_shield else 'None'
            show_exp = f'{self.exp} / {self.exp_to_next_lvl}'
            table = [['Level', self.lvl],['Name:', self.name], ['HP', self.hp], ['Attack Power',self.attack_power], ['Consumables', len(self)], ['Main-Hand', main_hand], ['Off-Hand', off_hand], ['Exp', show_exp]]
            print(f'\n=== {character_type} Sheet ==='.upper())
            print(tabulate(table, colalign=('center','center'), tablefmt='grid'))
            time.sleep(0.4)
        else:
            potion_chance = f'{self.potion_drop_chance * 100:.0f}%'
            drop_table = ", ".join(f'{weapon.name} ({int(chance * 100)}%)' for weapon, chance in self.drop_table) if self.drop_table else "None"
            table = [['Name:', self.name], ['HP', self.hp], ['Attack Power',self.attack_power], ['Potion Drop Chance', potion_chance], ['Drops', drop_table]]
            print(f'\n=== {character_type} Sheet ==='.upper())
            print(tabulate(table, colalign=('center','center') ,tablefmt='grid'))
            time.sleep(0.4)

    # Player class
class Player(Character):
    ''' Character info/stats/inventory '''
    def __init__(self, name: str, hp: int, attack_power: int) -> None:
        super().__init__(name, hp, attack_power)
        self.consumables_inventory = ['Potion', 'Potion', 'Potion']
        self.max_hp = hp
        self.equipped_weapon = None
        self.equipped_shield = None
        self.weapon_inventory = []
        self.lvl = 1
        self.exp = 0
        self.exp_to_next_lvl = 10

    # Inventory space
    def __len__(self) -> int:
        return len(self.consumables_inventory)
    
    # Potion usage
    def use_potion(self) -> None:
        ''' Potion usage functionality for healing '''
        if 'Potion' in self.consumables_inventory:
            heal_amount = round(self.max_hp * 0.3)
            self.hp += heal_amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f'You got healed for {heal_amount} HP by using a Potion!')
            self.consumables_inventory.remove('Potion')
        else:
            print('There is no Potions left in the inventory...')

    # Gear Equipment
    def equip_weapon(self, weapon: object) -> None:
            ''' Equipping main-hand weapon '''
            self.equipped_weapon = weapon
            print(f'\n{weapon.name} has been equipped!')

    def equip_shield(self, shield: object) -> None:
        ''' Equipping off-hand shield '''
        self.equipped_shield = shield
        print(f'\n{shield.name} has been equipped!')

    # Gained exp
    def gain_xp(self, amount: int) -> None:
        ''' Gaining exp function and leveling up once reaching the exp threshold'''
        self.exp += amount
        if amount > 0:
            print(f'\nYou have gained {amount} experience points!')
        while self.exp >= self.exp_to_next_lvl:
            self.level_up()
        
    # Leveling up
    def level_up(self) -> None:
        ''' Leveling up functionality '''
        self.lvl += 1
        divider()
        print(f'\nCongratulations, you have advanced to level: {self.lvl}!')
        divider()
        self.exp = self.exp - self.exp_to_next_lvl
        self.exp_to_next_lvl += 2
        self.attack_power += 1
        self.max_hp += 2
        self.hp = self.max_hp
        print(f'\nStats Increased:\n')
        print('Attack Power: +1 point')
        print('HP: +2 points')
        print(f'HP has been restored! {self.hp}/{self.hp}')