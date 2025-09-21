from simple_rpg_helpers import player_info, enemy_info, decide_turn, combat

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
    pass

class Enemy(Character):
    pass

# Character info
p_name, p_hp, p_power = player_info()
e_name, e_hp, e_power = enemy_info()
player = Player(p_name, p_hp, p_power)
enemy = Enemy(e_name, e_hp, e_power)
player.show_info()

# Dice roll for turn decision
attacker, defender = decide_turn(player, enemy)
# combat
combat(attacker, defender, player, enemy)

