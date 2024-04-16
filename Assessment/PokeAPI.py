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
