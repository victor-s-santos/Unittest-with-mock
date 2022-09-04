import unittest
from unittest.mock import patch, MagicMock
from pokemon_top import Pokemon

class TestPokemonApi(unittest.TestCase):
    def setUp(self):
        self.pokemon_name = "Pikachu"

    def test_format_return_types(self):
        """Must return a list instance."""
        pokemon_obj = Pokemon(pokemon_name="Pikachu")
        self.assertIsInstance(pokemon_obj.return_types(), list)


    @patch("pokemon_top.Pokemon.realize_get", return_value={"name": "Pikachu", "types": ["Eletric"]})
    @patch("pokemon_top.Pokemon.return_types", return_value=["Eletric"])
    def test_qnty_format(self, mocked_pokemon_list: MagicMock, mocked_pokemon_get: MagicMock):
        """Must return a int instance."""
        pokemon_obj = Pokemon(pokemon_name="Pikachu")
        self.assertIsInstance(pokemon_obj.number_of_types(), int)


if __name__ == "__main__":
    unittest.main()