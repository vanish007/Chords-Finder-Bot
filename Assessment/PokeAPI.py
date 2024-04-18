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
                PokeStats = PokemonStats(hp=hp, attack=attack, defense=defense, special_attack=special_attack, special_defense=special_defense, speed=speed)
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

