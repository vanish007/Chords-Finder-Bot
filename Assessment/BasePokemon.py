class BasePokemon:
    __name: str
    __instances: List[BasePokemon] = []

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__instances.append(self)

    def __str__(self) -> str:
        return f'Pokemon name is ' + color.BOLD + f'{self.__name}' + color.END
