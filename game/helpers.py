import random

# ----- Validation -----

def get_valid_input(prompt: str, options: list[str]) -> str:
    ''' Prompt user until valid option'''
    while True:
        user_input = input(prompt).strip().lower()
        if user_input not in options:
            print('\nInvalid input, try again')
        else:
            return user_input
        
def get_valid_name(prompt: str) -> str:
    ''' Prompt user for a valid name '''
    while True:
        user_input = input(prompt).strip()
        if user_input.isalpha():
            return user_input
        else:
            print('\nName cannot contain blank spaces, numbers, punctuation. Please type again.')

# ----- Character Creation -----

def player_info() -> tuple[str, int, int]:
    ''' Character creation with name input and randomized stats '''
    player_name = get_valid_name('\nPlease enter the name of your character: ').capitalize()
    player_hp = random.randint(13,16)
    player_power = random.randint(3,5)
    return player_name, player_hp, player_power

# ----- Damage application -----

def apply_damage(target, damage: int) -> None:
    '''Reduce target HP but not below 0'''
    target.hp -= damage
    target.hp = max(target.hp, 0)