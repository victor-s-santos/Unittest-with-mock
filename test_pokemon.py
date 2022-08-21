import unittest
from unittest.mock import patch, MagicMock
from pokemon_top import Pokemon

class TestPokemonApi(unittest.TestCase):
    def setUp(self):
        self.pokemon_name = "Pikachu"

    @patch("pokemon_top.Pokemon.realize_get")
    def test_format_return_types(self, mocked_pokemon_list):
        """Must return a list instance."""
        mocked_pokemon_list = MagicMock()
        mocked_pokemon_list.realize_get.return_value = [[
	{
		"number": "25",
		"name": "Pikachu",
		"species": "Mouse",
		"types": [
			"Electric"
	],}]
    ]
        pokemon_obj = Pokemon(pokemon_name="Pikachu")
        self.assertIsInstance(pokemon_obj.return_types(), list)


    @patch("pokemon_top.Pokemon.realize_get")
    @patch("pokemon_top.Pokemon.return_types")
    def test_qnty_format(self, mocked_pokemon_list: MagicMock, mocked_pokemon_get: MagicMock):
        """Must return a int instance."""
        mocked_pokemon_get.return_values = {"name": "Pikachu", "types": ["Eletric"]}
        mocked_pokemon_list.return_values = ["Eletric"]
        pokemon_obj = Pokemon(pokemon_name="Pikachu")
        self.assertIsInstance(pokemon_obj.number_of_types(), int)


if __name__ == "__main__":
    unittest.main()