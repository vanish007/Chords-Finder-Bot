@dataclass(frozen=True, slots=True)
class Pokemon(BasePokemon):
    id: int
    name: str
    height: int
    weight: int
    
    def __str__(self) -> str:
        return f'Pokemon name is ' + color.BOLD + f'{self.name}' + color.END + '\n' + \
               f'Pokemon ID is ' + color.BOLD + f'{self.id}' + color.END + '\n' + \
               f'Pokemon height is ' + color.BOLD + f'{self.height}' + color.END + '\n' + \
               f'Pokemon weight is ' + color.BOLD + f'{self.weight}' + color.END
