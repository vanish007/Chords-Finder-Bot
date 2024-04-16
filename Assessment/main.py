from __future__ import annotations
from typing import Union, List, Dict, Generator
import requests
from dataclasses import dataclass


cash: Dict[Union[str, int], Pokemon] = dict()
BasePokemonList: List[BasePokemon] = []
PokemonList: List[BasePokemon] = []

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

@dataclass(frozen=True, slots=True)
class BasePokemon:
    name: str

    def __str__(self) -> str:
        return f'Pokemon name is ' + color.BOLD + f'{self.name}' + color.END
    
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
                BasePoke = BasePokemon(name)
                Poke = Pokemon(id=id, name=name, height=height, weight=weight)
                cash[name] = Poke
                cash[id] = Poke
                BasePokemonList.append(BasePoke)
                PokemonList.append(Poke)
                return Poke
    
    @staticmethod
    def get_all(get_full: bool = False) -> Generator[BasePokemon, Pokemon]:
        try:
            if get_full == True:
                for data in PokemonList:
                    yield data
            else:
                for data in BasePokemonList:
                    yield data
        except:
            raise PokeError

## task 1 ##
ditto = PokeAPI.get_pokemon('ditto')
print(ditto)
print()

## task 2 ##
mx_weight, second_mx_weight = 0, 0
mx_name, second_mx_name = '', ''
for i in range(1, 51):
    poke = PokeAPI.get_pokemon(i)
    print(poke)
    print()
    if poke.weight >= mx_weight:
        second_mx_weight, second_mx_name = mx_weight, mx_name
        mx_weight, mx_name = poke.weight, poke.name
    elif poke.weight > second_mx_weight:
        second_mx_weight, second_mx_name = poke.weight, poke.name
print('The heaviest pokemon is ' + mx_name + ' with a total weight of ' + str(mx_weight) + '. '\
      'He is ' + str(mx_weight - second_mx_weight) + ' pokekilos heavier than second heaviest pokemon - ' + str(second_mx_name) + '.')
print()
