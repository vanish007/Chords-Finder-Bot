class Pokemon(BasePokemon):
    __id: int
    __name: str
    __height: int
    __weight: int
    __instances: List[Pokemon] = []

    def __init__(self, id: int, name: str, height: int, weight: int) -> None:
        self.__id = id
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__instances.append(self)

    def __str__(self) -> str:
        return f'Pokemon ID is ' + color.BOLD + f'{self.__id}' + color.END + '\n' + \
               f'Pokemon name is ' + color.BOLD + f'{self.__name}' + color.END + '\n' + \
               f'Pokemon height is ' + color.BOLD + f'{self.__height}' + color.END + '\n' + \
               f'Pokemon weight is ' + color.BOLD + f'{self.__weight}' + color.END
