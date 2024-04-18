@dataclass(frozen=True, slots=True)
class BasePokemon:
    name: str

    def __str__(self) -> str:
        return f'Pokemon name is ' + color.BOLD + f'{self.name}' + color.END
