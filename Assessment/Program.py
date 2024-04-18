from __future__ import annotations
from typing import Union, List, Dict, Generator
import requests
from dataclasses import dataclass
from time import sleep

cash: Dict[Union[str, int], Pokemon] = dict()
BasePokemonList: List[BasePokemon] = []
PokemonList: List[int] = []


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
               'Pokemon speed is ' + color.BOLD + f'{self.speed}' + color.END


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
                hp = pokemon_data['stats'][0]['base_stat']
                attack = pokemon_data['stats'][1]['base_stat']
                defense = pokemon_data['stats'][2]['base_stat']
                special_attack = pokemon_data['stats'][3]['base_stat']
                special_defense = pokemon_data['stats'][4]['base_stat']
                speed = pokemon_data['stats'][5]['base_stat']
                BasePoke = BasePokemon(name)
                PokeStats = PokemonStats(hp=hp, attack=attack, defense=defense, special_attack=special_attack,
                                         special_defense=special_defense, speed=speed)
                Poke = Pokemon(id=id, name=name, height=height, weight=weight, stats=PokeStats)
                cash[name] = Poke
                cash[id] = Poke
                BasePokemonList.append(BasePoke)
                PokemonList.append(id)
                return Poke

    @staticmethod
    def get_all(get_full: bool = False) -> Generator[BasePokemon, Pokemon]:
        try:
            if get_full == True:
                for data in PokemonList:
                    yield PokeAPI.get_pokemon(data)
            else:
                for data in BasePokemonList:
                    yield data
        except:
            raise PokeError


def ErrorMessage(num: int) -> str:
    if num == 1:
        return color.RED + color.BOLD + '####################################################\n'+\
        '#   Wrong input! Please enter number from 1 to 4   #\n' +\
        '####################################################' + color.END
    elif num == 2:
        return color.RED + color.BOLD + '##########################################\n'+\
               '#   Wrong input! Please enter a number   #\n'+\
              '##########################################' + color.END
    elif num == 3:
        return color.RED + color.BOLD + '#############################################\n'+\
               '#   Wrong input! Please enter digit 1 or 2  #\n'+\
               '#############################################' + color.END


print(color.BOLD + 'Hello! Welcome to my program. Choose your task:' + color.END)
print('1) Output "Ditto" pokemon')
print('2) Find the heaviest pokemon')
print('3) Output first N pokemons')
print('4) End the program')
num = 1
while True:
    print(color.BOLD + 'Enter a task number: ' + color.END, end='')
    try:
        num = int(input())
    except:
        print(ErrorMessage(1))
        continue
    if num == 1:
        print(color.YELLOW + '-----------task 1 begin----------' + color.END)
        print('Program is looking for information...')
        sleep(0.5)
        ditto = PokeAPI.get_pokemon('ditto')
        print('Done!')
        print()
        sleep(0.5)
        print(ditto)
        print(color.YELLOW + '-----------task 1 end------------' + color.END)
    elif num == 2:
        print(color.YELLOW + '-----------task 2 begin----------' + color.END)
        print('Program is looking for information...')
        sleep(0.5)
        mx_weight, second_mx_weight = 0, 0
        mx_name, second_mx_name = '', ''
        print('Currently processed pokemons:     0', end='')
        for i in range(1, 51):
            poke = PokeAPI.get_pokemon(i)
            if i < 10:
                print('\b\b', i, end='')
            else:
                print('\b\b\b', i, end='')
            if poke.weight >= mx_weight:
                second_mx_weight, second_mx_name = mx_weight, mx_name
                mx_weight, mx_name = poke.weight, poke.name
            elif poke.weight > second_mx_weight:
                second_mx_weight, second_mx_name = poke.weight, poke.name
        print()
        print('Done!')
        print()
        sleep(0.5)
        print(color.BOLD + 'The heaviest pokemon is ' + mx_name + \
              ' with a total weight of ' + str(mx_weight) + '. ' \
            'He is ' + str(mx_weight - second_mx_weight) + \
              ' pokekilos heavier than second heaviest pokemon - ' + str(second_mx_name) + '.' + color.END)
        print(color.YELLOW + '-----------task 2 end------------' + color.END)
    elif num == 3:
        print(color.YELLOW + '-----------task 3 begin----------' + color.END)
        while True:
            print(color.BOLD + 'Enter N: ' + color.END, end='')
            try:
                n = int(input())
                break
            except:
                print(ErrorMessage(2))
                continue
        print('Program is looking for information...')
        print('Currently processed pokemons:     0', end='')
        for i in range(1, n + 1):
            temp = PokeAPI.get_pokemon(i)
            if i < 10:
                print('\b\b', i, end='')
            elif i < 100:
                print('\b\b\b', i, end='')
            elif i < 1000:
                print('\b\b\b\b', i, end='')
            else:
                print('\b\b\b\b\b', i, end='')
        sleep(0.5)
        print()
        print('Done!')
        sleep(0.5)
        print(color.BOLD + 'Do you want to see full info?' + color.END)
        print('1) Yes')
        print('2) No')
        while True:
            print(color.BOLD + 'Enter your answer: ' + color.END, end='')
            try:
                ans = int(input())
            except:
                print(ErrorMessage(3))
                continue
            if ans == 1:
                for n, i in enumerate(PokeAPI.get_all(True)):
                    print(f'{n+1}: ')
                    print(i)
                break
            elif ans == 2:
                for n, i in enumerate(PokeAPI.get_all(False)):
                    print(f'{n+1}: {i}')
                break
            else:
                print(ErrorMessage(3))
                continue
        print(color.YELLOW + '-----------task 3 end------------' + color.END)
    elif num == 4:
        print(color.YELLOW + 'Goodbye, have a good day!' + color.END, end='')
        break
    else:
        print(ErrorMessage(1))
        continue
