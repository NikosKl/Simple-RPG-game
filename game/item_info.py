from game.weapons import Dagger, Shortsword, Wooden_Shield, Iron_Shield
from tabulate import tabulate

def weapon_info() -> None:
    ''' Display weapon stats in a table '''
    headers = ['Weapon', 'Damage', 'Crit Chance', 'Crit Damage']
    dagger_min_damage, dagger_max_damage = Dagger.weapon_damage
    shortsword_min_damage, shortsword_max_damage = Shortsword.weapon_damage
    weapon_table = [[Dagger.name, f'{dagger_min_damage} - {dagger_max_damage}', f'{Dagger.crit_chance * 100:.0f}%', f'x{Dagger.crit_modifier}']
                   ,[Shortsword.name, f'{shortsword_min_damage} - {shortsword_max_damage}', f'{Shortsword.crit_chance * 100:.0f}%', f'x{Shortsword.crit_modifier}']]
    print('\n' + tabulate(weapon_table, headers=headers, colalign=('center', 'center', 'center', 'center'), tablefmt='grid'))

def shield_info() -> None:
    ''' Display Shield stats in a table '''
    headers = ['Weapon', 'Block Chance']
    shield_table = [[Wooden_Shield.name, f'{Wooden_Shield.block_chance * 100:.0f}%'], [Iron_Shield.name, f'{Iron_Shield.block_chance * 100:.0f}%']]
    print('\n' + tabulate(shield_table, headers=headers, colalign=('center', 'center'), tablefmt='grid'))
    
