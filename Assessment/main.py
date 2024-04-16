from __future__ import annotations
from typing import Union, List, Dict, Generator
import requests


cash: Dict[Union[str, int], Pokemon] = dict()


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


class BasePokemon:
    __name: str
    __instances: List[BasePokemon] = []

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__instances.append(self)

    def __str__(self) -> str:
        return f'Pokemon name is ' + color.BOLD + f'{self.__name}' + color.END
    

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
 

class PokeError(Exception):
    def __init__(self, *args, **kwargs):
        if args:
            self.message = args[0]
        elif kwargs:
            self.message = kwargs[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return f'Error occured while working with PokeAPI'


class PokeAPI:
    @staticmethod
    def get_pokemon(id_or_name: Union[int, str]) -> Pokemon:
        if id_or_name in cash:
            return cash[id_or_name]
        else:
            try:
                pokemon_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id_or_name}').json()
            except:
                raise PokeError('Unexisting id or name') from None
            else:
                id = pokemon_data['id']
                name = pokemon_data['name']
                height = pokemon_data['height']
                weight = pokemon_data['weight']
                BasePokemon(name)
                Poke = Pokemon(id, name, height, weight)
                cash[name] = Poke
                cash[int(id)] = Poke
                cash[str(id)] = Poke
                return Poke
    
    @staticmethod
    def get_all(get_full: bool = False) -> Generator[BasePokemon, Pokemon]:
        try:
            if get_full == True:
                for data in Pokemon._Pokemon__instances:
                    yield data
            else:
                for data in BasePokemon._BasePokemon__instances:
                    yield data
        except:
            raise PokeError

# ## task 1 ##
# ditto = PokeAPI.get_pokemon('ditto')
# print(ditto)

# ## task 2 ##
# mx_weight, second_mx_weight = 0, 0
# mx_name, second_mx_name = '', ''
# for i in range(1, 51):
#     poke = PokeAPI.get_pokemon(i)
#     poke_weight = poke._Pokemon__weight
#     poke_name = poke._Pokemon__name
#     if poke_weight >= mx_weight:
#         second_mx_weight, second_mx_name = mx_weight, mx_name
#         mx_weight, mx_name = poke_weight, poke_name
#     elif poke_weight > second_mx_weight:
#         second_mx_weight, second_mx_name = poke_weight, poke_name
# print('The heaviest pokemon is ' + mx_name + ' with a total weight of ' + str(mx_weight) + '. '\
#       'He is ' + str(mx_weight - second_mx_weight) + ' pokekilos heavier than second heaviest pokemon - ' + str(second_mx_name) + '.')
