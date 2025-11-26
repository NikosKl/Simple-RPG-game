class Weapon():
    def __init__(self, name: str, weapon_damage: tuple[int, int], item_type: str, crit_chance: float, crit_modifier: int) -> None:
        self.name = name
        self.weapon_damage = weapon_damage
        self.item_type = item_type
        self.crit_chance = crit_chance
        self.crit_modifier = crit_modifier

# Weapons
Dagger = Weapon('Dagger', (1,2), 'Main-Hand', 0.35, 2)
Shortsword = Weapon('Shortsword', (1,3), 'Main-Hand', 0.25, 2)

class Shield():
    def __init__(self, name: str, block_chance: float, item_type: str) -> None:
        self.name = name
        self.block_chance = block_chance
        self.item_type = item_type

Wooden_Shield = Shield('Wooden Shield', 0.25, 'Off-Hand')
Iron_Shield = Shield('Iron Shield', 0.30, 'Off-Hand')


def create_weapon(name: str) -> Weapon | Shield | None:
    if name == 'Dagger':
        return Dagger
    elif name == 'Shortsword':
        return Shortsword
    elif name == 'Wooden Shield':
        return Wooden_Shield
    elif name == 'Iron Shield':
        return Iron_Shield
    else:
        return None