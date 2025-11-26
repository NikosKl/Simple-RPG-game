from game.player import Character

class Enemy(Character):
    ''' Enemy character '''
    def __init__(self, name: str, hp: int, attack_power: int, potion_drop_chance: float, exp: int, drop_table: list | None = None) -> None:
        super().__init__(name, hp, attack_power)
        self.potion_drop_chance = potion_drop_chance
        self.drop_table = drop_table
        self.exp = exp