import random
from game.weapons import Shortsword, Dagger, Wooden_Shield, Iron_Shield
from game.enemy import Enemy

# List of Enemies
def common_enemies() -> tuple[str, int, int, float, int, list]:
    enemies = [
        ('Goblin Soldier', random.randint(6,7), random.randint(3,4), 0.35, 3, [(Dagger, 0.4), (Wooden_Shield, 0.35), (Shortsword, 0.05)]),
        ('Dire Wolf', random.randint(4,6), random.randint(2,3), 0.6, 3, []),
        ('Skeleton Archer', random.randint(5,6), random.randint(2,4), 0.35, 4, [(Dagger, 0.4), (Wooden_Shield, 0.35), (Shortsword, 0.05)]),
        ('Bandit', random.randint(5,6), random.randint(3,5), 0.4, 4, [(Dagger, 0.4), (Wooden_Shield, 0.35), (Shortsword, 0.1)])
        ]
    return random.choice(enemies)

def elite_enemies() -> tuple[str, int, int, float, int, list]:
    elites = [
        ('Dire Wolf', random.randint(8,10), random.randint(4,5), 0.7, 6, []),
        ('Orc General', random.randint(11,13), random.randint(5,6), 0.5, 6, [(Shortsword, 0.4), (Iron_Shield, 0.3)]),
        ('Skeleton Priest', random.randint(10,12), random.randint(4,6), 0.5, 6, [(Shortsword, 0.4), (Iron_Shield, 0.25)])
    ]
    return random.choice(elites)

def boss() -> tuple[str, int, int, float, int, list]:
    name = 'Chimera'
    hp = random.randint(20,25)
    power = random.randint(7,8)
    potion_drop_chance = 0
    drop_table = []
    exp = 0
    return name, hp, power, potion_drop_chance, exp, drop_table


def generate_enemy(name: str) -> Enemy | None:
    for i in range(10):
        enemy = common_enemies()
        if enemy[0] == name:
            return Enemy(*enemy)
        
    for i in range(10):
        enemy = elite_enemies()
        if enemy[0] == name:
            return Enemy(*enemy)
        
    if name == 'Chimera':
        return Enemy(*boss())
    
    return None