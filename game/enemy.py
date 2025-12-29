from game.player import Character
from tabulate import tabulate
import time

class Enemy(Character):
    ''' Enemy character '''
    def __init__(self, name: str, hp: int, attack_power: int, potion_drop_chance: float, exp: int, drop_table: list | None = None) -> None:
        super().__init__(name, hp, attack_power)
        self.potion_drop_chance = potion_drop_chance
        self.drop_table = drop_table
        self.exp = exp

    def show_info(self) -> None:
        potion_chance = f'{self.potion_drop_chance * 100:.0f}%'
        drop_table = ", ".join(f'{weapon.name} ({int(chance * 100)}%)' for weapon, chance in self.drop_table) if self.drop_table else "None"
        table = [['Name:', self.name], ['HP', self.hp], ['Attack Power',self.attack_power], ['Potion Drop Chance', potion_chance], ['Drops', drop_table]]
        print(f'\n=== Enemy Sheet ==='.upper())
        print(tabulate(table, colalign=('center','center') ,tablefmt='grid'))
        time.sleep(0.4)