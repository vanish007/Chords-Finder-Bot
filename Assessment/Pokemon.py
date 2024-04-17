@dataclass(frozen=True, slots=True)
class Pokemon(BasePokemon):
    id: int
    name: str
    height: int
    weight: int
    stats: PokemonStats
    
    def __str__(self) -> str:
        return 'Pokemon name is ' + color.BOLD + f'{self.name}' + color.END + '\n' + \
               'Pokemon ID is ' + color.BOLD + f'{self.id}' + color.END + '\n' + \
               'Pokemon height is ' + color.BOLD + f'{self.height}' + color.END + '\n' + \
               'Pokemon weight is ' + color.BOLD + f'{self.weight}' + color.END + '\n' + \
                f'{self.stats}'
