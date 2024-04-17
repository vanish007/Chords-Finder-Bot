@dataclass(frozen=True, slots=True)
class PokemonStats:
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    
    def __str__(self) -> str:
        return 'Pokemon hp is ' + color.BOLD + f'{self.hp}' + color.END + '\n' + \
               'Pokemon attack is ' + color.BOLD + f'{self.attack}' + color.END + '\n' + \
               'Pokemon defense is ' + color.BOLD + f'{self.defense}' + color.END + '\n' + \
               'Pokemon special attack is ' + color.BOLD + f'{self.special_attack}' + color.END + '\n' + \
               'Pokemon special defense is ' + color.BOLD + f'{self.special_defense}' + color.END + '\n' + \
               'Pokemon speed is '+ color.BOLD + f'{self.speed}' + color.END
