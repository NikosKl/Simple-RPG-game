from simple_rpg_helpers import player_info, lvl1_enemy, lvl2_enemy, boss, decide_turn, combat, get_valid_input

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        attacker = self.__class__.__name__
        defender = target.__class__.__name__

        target.hp -= self.attack_power
        print(f'({attacker}) {self.name} attacks {target.name} for {self.attack_power} damage!')
        print(f'({defender}) {target.name} remaining HP: {target.hp}')
        if target.hp <= 0:
            target.hp = 0

    def is_alive(self):
        return self.hp > 0

    def show_info(self):
        character_type = self.__class__.__name__
        print(f'\n{character_type} Sheet\n'.upper())
        print(f'Name: {self.name}')
        print(f'HP: {self.hp}')
        print(f'Attack Power: {self.attack_power}')
        
class Player(Character):

    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.inventory = ['Potion', 'Potion', 'Potion']
        self.max_hp = hp

    def __len__(self):
        return len(self.inventory)
    
    def use_potion(self):
        if 'Potion' in self.inventory:
            heal_amount = round(self.max_hp * 0.3)
            self.hp += heal_amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f'You got healed for {heal_amount} HP by using a Potion!')
            player.inventory.remove('Potion')
        else:
            print('There is no Potions in the inventory...')

    
class Enemy(Character):
    pass

# Character info
p_name, p_hp, p_power = player_info()
player = Player(p_name, p_hp, p_power)
player.show_info()

print(f'Inventory: {len(player)} Potions')

all_enemies = []

lvl1_stats = lvl1_enemy()
all_enemies.extend([Enemy(name, hp, power) for (name, hp, power) in lvl1_stats])

lvl2_stats = lvl2_enemy()
all_enemies.extend([Enemy(name, hp, power) for (name, hp, power) in lvl2_stats])

boss_stats = boss()
all_enemies.append(Enemy(*boss_stats))

for i, enemy in enumerate(all_enemies):
    if not player.is_alive():
        break
    # Dice roll for turn decision
    attacker, defender = decide_turn(player, enemy)
    # combat
    combat(attacker, defender, player, enemy)

    if not player.is_alive():
        break

    if i < len(all_enemies) - 1:
        if player.hp < player.max_hp and len(player.inventory) > 0:
            print(f'\nALERT!: {player.name} remaining HP: {player.hp}')
            print('\nA potion will be used to replenish your hp')
            player.use_potion()
            print(f'Inventory: {len(player)} Potions left')