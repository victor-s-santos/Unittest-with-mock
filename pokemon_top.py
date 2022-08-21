import types
import requests

class Pokemon:
    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name
        self.api_call = f"https://pokeapi.glitch.me/v1/pokemon/{self.pokemon_name}/"

    def realize_get(self):
        r = requests.get(self.api_call)
        return r.json()

    def return_types(self) -> list:
        _types = self.realize_get()[0]["types"]
        return _types

    def number_of_types(self) -> int:
        returned_types = self.return_types()
        return len(returned_types)
    

#poke = Pokemon(pokemon_name="Pikachu")
#poke.number_of_types()
